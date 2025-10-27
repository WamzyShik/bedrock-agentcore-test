#!/usr/bin/env python3
"""
Test Suite Validation Script

This script runs the test suite with the new structure and compares results
against the baseline (if available). It validates:
1. Test discovery works correctly
2. Tests can be executed
3. No regressions compared to baseline
4. Documents any issues found

Usage:
    python scripts/reorganization/validate_test_suite.py
"""

import subprocess
import json
import datetime
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple


class TestSuiteValidator:
    """Validates the test suite after reorganization."""
    
    def __init__(self):
        self.output_dir = Path("scripts/reorganization")
        self.baseline_file = self.output_dir / "baseline_test_discovery.json"
        self.validation_file = self.output_dir / "test_validation_results.json"
        self.report_file = self.output_dir / "TEST_VALIDATION_REPORT.md"
        
    def load_baseline(self) -> Dict[str, Any]:
        """Load baseline test results if available."""
        if self.baseline_file.exists():
            with open(self.baseline_file, "r") as f:
                return json.load(f)
        return None
    
    def run_test_discovery(self) -> Dict[str, Any]:
        """Run pytest test discovery."""
        print("Running test discovery...")
        print("=" * 80)
        
        result = subprocess.run(
            ["python", "-m", "pytest", "tests/", "--collect-only", "-q"],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Parse output to count tests
        test_count = 0
        lines = result.stdout.split('\n')
        for line in lines:
            if 'test' in line.lower() and '::' in line:
                test_count += 1
        
        discovery_result = {
            "timestamp": datetime.datetime.now().isoformat(),
            "return_code": result.returncode,
            "test_count": test_count,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": result.returncode == 0 or result.returncode == 5
        }
        
        print(f"Test discovery return code: {result.returncode}")
        print(f"Tests discovered: {test_count}")
        print(f"Success: {discovery_result['success']}")
        
        return discovery_result
    
    def run_test_execution(self) -> Dict[str, Any]:
        """Run actual test execution."""
        print("\n" + "=" * 80)
        print("Running test execution...")
        print("=" * 80)
        
        result = subprocess.run(
            ["python", "-m", "pytest", "tests/", 
             "-v", "--tb=short", "-x"],  # Stop on first failure
            capture_output=True,
            text=True,
            timeout=300
        )
        
        # Parse test results
        passed = result.stdout.count(" PASSED")
        failed = result.stdout.count(" FAILED")
        skipped = result.stdout.count(" SKIPPED")
        errors = result.stdout.count(" ERROR")
        
        execution_result = {
            "timestamp": datetime.datetime.now().isoformat(),
            "return_code": result.returncode,
            "passed": passed,
            "failed": failed,
            "skipped": skipped,
            "errors": errors,
            "total": passed + failed + skipped + errors,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": result.returncode == 0
        }
        
        print(f"Test execution return code: {result.returncode}")
        print(f"Passed: {passed}, Failed: {failed}, Skipped: {skipped}, Errors: {errors}")
        print(f"Success: {execution_result['success']}")
        
        return execution_result
    
    def check_test_discovery_issues(self, discovery: Dict[str, Any]) -> List[str]:
        """Check for test discovery issues."""
        issues = []
        
        if not discovery['success']:
            issues.append("Test discovery failed with non-zero return code")
        
        if discovery['test_count'] == 0:
            issues.append("No tests were discovered")
        
        if 'error' in discovery['stderr'].lower():
            issues.append("Errors found in test discovery stderr")
        
        if 'importerror' in discovery['stdout'].lower() or 'importerror' in discovery['stderr'].lower():
            issues.append("Import errors detected during test discovery")
        
        if 'modulenotfounderror' in discovery['stdout'].lower() or 'modulenotfounderror' in discovery['stderr'].lower():
            issues.append("Module not found errors detected")
        
        return issues
    
    def compare_with_baseline(self, current: Dict[str, Any], baseline: Dict[str, Any]) -> Dict[str, Any]:
        """Compare current results with baseline."""
        if not baseline:
            return {
                "baseline_available": False,
                "message": "No baseline available for comparison"
            }
        
        comparison = {
            "baseline_available": True,
            "baseline_timestamp": baseline.get('timestamp', 'Unknown'),
            "current_timestamp": current['timestamp'],
            "changes": []
        }
        
        # Compare test counts if available
        baseline_count = baseline.get('test_count', 0)
        current_count = current.get('test_count', 0)
        
        if baseline_count != current_count:
            comparison['changes'].append(
                f"Test count changed: {baseline_count} -> {current_count} "
                f"(diff: {current_count - baseline_count:+d})"
            )
        
        # Compare success status
        baseline_success = baseline.get('success', False)
        current_success = current.get('success', False)
        
        if baseline_success != current_success:
            comparison['changes'].append(
                f"Success status changed: {baseline_success} -> {current_success}"
            )
        
        return comparison
    
    def generate_report(self, discovery: Dict[str, Any], execution: Dict[str, Any], 
                       comparison: Dict[str, Any], issues: List[str]) -> str:
        """Generate a markdown report of the validation."""
        report = []
        report.append("# Test Suite Validation Report")
        report.append("")
        report.append(f"**Generated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Summary
        report.append("## Summary")
        report.append("")
        if not issues and execution['success']:
            report.append("✅ **Test suite validation PASSED**")
        else:
            report.append("❌ **Test suite validation FAILED**")
        report.append("")
        
        # Test Discovery
        report.append("## Test Discovery")
        report.append("")
        report.append(f"- **Status:** {'✅ Success' if discovery['success'] else '❌ Failed'}")
        report.append(f"- **Tests Discovered:** {discovery['test_count']}")
        report.append(f"- **Return Code:** {discovery['return_code']}")
        report.append("")
        
        # Test Execution
        report.append("## Test Execution")
        report.append("")
        report.append(f"- **Status:** {'✅ Success' if execution['success'] else '❌ Failed'}")
        report.append(f"- **Passed:** {execution['passed']}")
        report.append(f"- **Failed:** {execution['failed']}")
        report.append(f"- **Skipped:** {execution['skipped']}")
        report.append(f"- **Errors:** {execution['errors']}")
        report.append(f"- **Total:** {execution['total']}")
        report.append(f"- **Return Code:** {execution['return_code']}")
        report.append("")
        
        # Baseline Comparison
        report.append("## Baseline Comparison")
        report.append("")
        if comparison['baseline_available']:
            report.append(f"- **Baseline Timestamp:** {comparison['baseline_timestamp']}")
            report.append("")
            if comparison['changes']:
                report.append("### Changes Detected:")
                report.append("")
                for change in comparison['changes']:
                    report.append(f"- {change}")
            else:
                report.append("✅ No significant changes detected from baseline")
        else:
            report.append(f"ℹ️ {comparison['message']}")
        report.append("")
        
        # Issues
        if issues:
            report.append("## Issues Found")
            report.append("")
            for i, issue in enumerate(issues, 1):
                report.append(f"{i}. ❌ {issue}")
            report.append("")
        else:
            report.append("## Issues Found")
            report.append("")
            report.append("✅ No issues detected")
            report.append("")
        
        # Recommendations
        report.append("## Recommendations")
        report.append("")
        if not issues and execution['success']:
            report.append("- ✅ Test suite is working correctly with the new structure")
            report.append("- ✅ All tests are discoverable")
            report.append("- ✅ Test execution is successful")
            report.append("- ✅ Ready to proceed with next reorganization tasks")
        else:
            report.append("### Action Items:")
            report.append("")
            if not discovery['success']:
                report.append("1. Fix test discovery issues")
                report.append("   - Check pytest configuration in pyproject.toml")
                report.append("   - Verify test file naming conventions")
                report.append("   - Check for import errors")
            if execution['failed'] > 0:
                report.append("2. Fix failing tests")
                report.append("   - Review test output for specific failures")
                report.append("   - Update test imports if needed")
                report.append("   - Verify test fixtures are accessible")
            if 'import' in ' '.join(issues).lower():
                report.append("3. Fix import errors")
                report.append("   - Run import validation script")
                report.append("   - Update module paths")
                report.append("   - Check __init__.py files")
        report.append("")
        
        # Test Output
        report.append("## Test Discovery Output")
        report.append("")
        report.append("```")
        report.append(discovery['stdout'][:2000])  # Limit output
        if len(discovery['stdout']) > 2000:
            report.append("... (output truncated)")
        report.append("```")
        report.append("")
        
        if execution['failed'] > 0 or execution['errors'] > 0:
            report.append("## Test Execution Output (Failures)")
            report.append("")
            report.append("```")
            # Extract failure information
            lines = execution['stdout'].split('\n')
            failure_section = False
            failure_lines = []
            for line in lines:
                if 'FAILED' in line or 'ERROR' in line:
                    failure_section = True
                if failure_section:
                    failure_lines.append(line)
                    if len(failure_lines) > 100:  # Limit output
                        break
            report.append('\n'.join(failure_lines))
            report.append("```")
            report.append("")
        
        return '\n'.join(report)
    
    def save_results(self, discovery: Dict[str, Any], execution: Dict[str, Any], 
                    comparison: Dict[str, Any], issues: List[str]):
        """Save validation results to JSON file."""
        results = {
            "timestamp": datetime.datetime.now().isoformat(),
            "discovery": discovery,
            "execution": execution,
            "comparison": comparison,
            "issues": issues,
            "overall_success": not issues and execution['success']
        }
        
        with open(self.validation_file, "w") as f:
            json.dump(results, f, indent=2)
        
        print(f"\nValidation results saved to: {self.validation_file}")
    
    def save_report(self, report: str):
        """Save markdown report."""
        with open(self.report_file, "w") as f:
            f.write(report)
        
        print(f"Validation report saved to: {self.report_file}")
    
    def run_validation(self) -> bool:
        """Run complete validation process."""
        print("=" * 80)
        print("TEST SUITE VALIDATION")
        print("=" * 80)
        print()
        
        # Load baseline
        baseline = self.load_baseline()
        if baseline:
            print(f"✓ Baseline loaded from {self.baseline_file}")
        else:
            print(f"ℹ No baseline found at {self.baseline_file}")
        print()
        
        # Run test discovery
        discovery = self.run_test_discovery()
        
        # Check for discovery issues
        issues = self.check_test_discovery_issues(discovery)
        
        # Run test execution (only if discovery succeeded)
        if discovery['success']:
            execution = self.run_test_execution()
        else:
            print("\n⚠️ Skipping test execution due to discovery failures")
            execution = {
                "timestamp": datetime.datetime.now().isoformat(),
                "return_code": -1,
                "passed": 0,
                "failed": 0,
                "skipped": 0,
                "errors": 0,
                "total": 0,
                "stdout": "",
                "stderr": "",
                "success": False
            }
        
        # Compare with baseline
        comparison = self.compare_with_baseline(discovery, baseline)
        
        # Generate report
        report = self.generate_report(discovery, execution, comparison, issues)
        
        # Save results
        self.save_results(discovery, execution, comparison, issues)
        self.save_report(report)
        
        # Print summary
        print("\n" + "=" * 80)
        print("VALIDATION SUMMARY")
        print("=" * 80)
        print()
        if not issues and execution['success']:
            print("✅ Test suite validation PASSED")
            print(f"   - {discovery['test_count']} tests discovered")
            print(f"   - {execution['passed']} tests passed")
            if execution['skipped'] > 0:
                print(f"   - {execution['skipped']} tests skipped")
            return True
        else:
            print("❌ Test suite validation FAILED")
            print(f"   - Issues found: {len(issues)}")
            if execution['failed'] > 0:
                print(f"   - Failed tests: {execution['failed']}")
            if execution['errors'] > 0:
                print(f"   - Test errors: {execution['errors']}")
            print()
            print("See detailed report at:")
            print(f"   {self.report_file}")
            return False


def main():
    """Main entry point."""
    validator = TestSuiteValidator()
    success = validator.run_validation()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
