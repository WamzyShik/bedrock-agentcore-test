#!/usr/bin/env python3
"""
Final Comprehensive Validation Script

This script runs all validation checks to ensure the repository reorganization
is complete and successful.

Task: 13.3 Run final comprehensive validation
Requirements: 1.3, 1.4, 11.5, 13.5
"""

import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


def run_command(cmd: List[str], description: str) -> Dict[str, Any]:
    """Run a command and return the result."""
    print(f"\n{'='*80}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print(f"{'='*80}\n")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        return {
            "success": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "description": description
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "returncode": -1,
            "stdout": "",
            "stderr": "Command timed out after 5 minutes",
            "description": description
        }
    except Exception as e:
        return {
            "success": False,
            "returncode": -1,
            "stdout": "",
            "stderr": str(e),
            "description": description
        }


def print_result(result: Dict[str, Any]):
    """Print the result of a validation check."""
    status = "✅ PASS" if result["success"] else "❌ FAIL"
    print(f"\n{status}: {result['description']}")
    
    if not result["success"]:
        print(f"\nError output:")
        print(result["stderr"][:500])  # First 500 chars of error


def final_validation():
    """Run all final validation checks."""
    
    print("=" * 80)
    print("FINAL COMPREHENSIVE VALIDATION")
    print("=" * 80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "checks": [],
        "summary": {
            "total": 0,
            "passed": 0,
            "failed": 0
        }
    }
    
    # Define all validation checks
    checks = [
        {
            "cmd": ["python", "scripts/reorganization/test_current_env_imports.py"],
            "description": "Import Validation - All modules importable"
        },
        {
            "cmd": ["python", "scripts/reorganization/validate_examples.py"],
            "description": "Examples Validation - All examples have valid syntax"
        },
        {
            "cmd": ["python", "scripts/reorganization/validate_cicd.py"],
            "description": "CI/CD Validation - Pipeline configuration correct"
        },
        {
            "cmd": ["python", "-m", "pytest", "tests/", "--co", "-q"],
            "description": "Test Discovery - All tests discoverable"
        },
    ]
    
    # Run all checks
    for check in checks:
        result = run_command(check["cmd"], check["description"])
        results["checks"].append(result)
        results["summary"]["total"] += 1
        
        if result["success"]:
            results["summary"]["passed"] += 1
        else:
            results["summary"]["failed"] += 1
        
        print_result(result)
    
    # Additional manual checks
    print(f"\n{'='*80}")
    print("MANUAL VERIFICATION CHECKS")
    print(f"{'='*80}\n")
    
    manual_checks = []
    
    # Check for key files
    key_files = [
        "README.md",
        "MIGRATION.md",
        "REORGANIZATION_SUMMARY.md",
        "pyproject.toml",
        ".github/workflows/ci-cd.yml",
        "src/fraud_detection/__init__.py",
        "tests/conftest.py",
        "docs/README.md",
        "examples/README.md",
        "infrastructure/README.md",
        "scripts/README.md",
        ".archive/README.md"
    ]
    
    print("Checking for key files...")
    missing_files = []
    for file_path in key_files:
        path = Path(file_path)
        if path.exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} (missing)")
            missing_files.append(file_path)
    
    manual_checks.append({
        "check": "Key files exist",
        "passed": len(missing_files) == 0,
        "details": f"Missing: {missing_files}" if missing_files else "All key files present"
    })
    
    # Check for key directories
    print(f"\nChecking for key directories...")
    key_dirs = [
        "src/fraud_detection",
        "tests/unit",
        "tests/integration",
        "infrastructure/aws",
        "examples",
        "docs",
        "scripts",
        ".archive"
    ]
    
    missing_dirs = []
    for dir_path in key_dirs:
        path = Path(dir_path)
        if path.exists() and path.is_dir():
            print(f"  ✅ {dir_path}/")
        else:
            print(f"  ❌ {dir_path}/ (missing)")
            missing_dirs.append(dir_path)
    
    manual_checks.append({
        "check": "Key directories exist",
        "passed": len(missing_dirs) == 0,
        "details": f"Missing: {missing_dirs}" if missing_dirs else "All key directories present"
    })
    
    # Check package installation
    print(f"\nChecking package installation...")
    try:
        import fraud_detection
        print(f"  ✅ fraud_detection package importable")
        manual_checks.append({
            "check": "Package installation",
            "passed": True,
            "details": "fraud_detection package is importable"
        })
    except ImportError as e:
        print(f"  ❌ Cannot import fraud_detection: {e}")
        manual_checks.append({
            "check": "Package installation",
            "passed": False,
            "details": f"Import error: {e}"
        })
    
    results["manual_checks"] = manual_checks
    
    # Summary
    print(f"\n{'='*80}")
    print("VALIDATION SUMMARY")
    print(f"{'='*80}\n")
    
    print(f"Automated Checks:")
    print(f"  Total: {results['summary']['total']}")
    print(f"  Passed: {results['summary']['passed']}")
    print(f"  Failed: {results['summary']['failed']}")
    
    manual_passed = sum(1 for c in manual_checks if c["passed"])
    manual_total = len(manual_checks)
    print(f"\nManual Checks:")
    print(f"  Total: {manual_total}")
    print(f"  Passed: {manual_passed}")
    print(f"  Failed: {manual_total - manual_passed}")
    
    # Overall result
    all_passed = (
        results['summary']['failed'] == 0 and
        all(c["passed"] for c in manual_checks)
    )
    
    print(f"\n{'='*80}")
    if all_passed:
        print("✅ OVERALL: ALL VALIDATIONS PASSED")
        print("The repository reorganization is complete and successful!")
    else:
        print("⚠️  OVERALL: SOME VALIDATIONS FAILED")
        print("Please review the failed checks above.")
    print(f"{'='*80}")
    
    results["overall_success"] = all_passed
    results["completed"] = datetime.now().isoformat()
    
    return results


def save_results(results: Dict[str, Any]):
    """Save validation results to JSON file."""
    output_file = Path(__file__).parent / "final_validation_results.json"
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to: {output_file}")


def create_validation_report(results: Dict[str, Any]):
    """Create a human-readable validation report."""
    report_file = Path(__file__).parent / "FINAL_VALIDATION_REPORT.md"
    
    report = f"""# Final Validation Report

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Status:** {'✅ PASSED' if results['overall_success'] else '❌ FAILED'}

---

## Automated Validation Checks

| Check | Status | Description |
|-------|--------|-------------|
"""
    
    for check in results["checks"]:
        status = "✅ Pass" if check["success"] else "❌ Fail"
        report += f"| {status} | {check['returncode']} | {check['description']} |\n"
    
    report += f"""
**Summary:** {results['summary']['passed']}/{results['summary']['total']} checks passed

---

## Manual Verification Checks

| Check | Status | Details |
|-------|--------|---------|
"""
    
    for check in results.get("manual_checks", []):
        status = "✅ Pass" if check["passed"] else "❌ Fail"
        report += f"| {status} | {check['check']} | {check['details']} |\n"
    
    manual_passed = sum(1 for c in results.get("manual_checks", []) if c["passed"])
    manual_total = len(results.get("manual_checks", []))
    
    report += f"""
**Summary:** {manual_passed}/{manual_total} checks passed

---

## Overall Result

"""
    
    if results['overall_success']:
        report += """✅ **ALL VALIDATIONS PASSED**

The repository reorganization has been completed successfully. All automated and manual checks have passed.

### Next Steps

1. Review the validation results
2. Commit all changes
3. Create a pull request for review
4. Merge to main branch after approval

"""
    else:
        report += """⚠️  **SOME VALIDATIONS FAILED**

Please review the failed checks above and address any issues before proceeding.

### Recommended Actions

1. Review failed checks in detail
2. Fix any identified issues
3. Re-run validation
4. Proceed only when all checks pass

"""
    
    report += f"""---

## Validation Details

- **Started:** {results['timestamp']}
- **Completed:** {results['completed']}
- **Total Checks:** {results['summary']['total'] + len(results.get('manual_checks', []))}
- **Passed:** {results['summary']['passed'] + sum(1 for c in results.get('manual_checks', []) if c['passed'])}
- **Failed:** {results['summary']['failed'] + sum(1 for c in results.get('manual_checks', []) if not c['passed'])}

---

*This report was automatically generated by the final validation script.*
"""
    
    with open(report_file, "w") as f:
        f.write(report)
    
    print(f"Validation report saved to: {report_file}")


if __name__ == "__main__":
    try:
        results = final_validation()
        save_results(results)
        create_validation_report(results)
        
        sys.exit(0 if results["overall_success"] else 1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
