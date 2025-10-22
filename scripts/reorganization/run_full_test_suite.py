#!/usr/bin/env python3
"""
Run full test suite and compare against baseline.
This validates that the reorganization hasn't broken any tests.
"""

import subprocess
import json
import datetime
from pathlib import Path
import sys

def load_baseline():
    """Load baseline test results if available."""
    baseline_file = Path("scripts/reorganization/baseline_test_discovery.json")
    if baseline_file.exists():
        with open(baseline_file, "r") as f:
            return json.load(f)
    return None

def run_test_suite():
    """Run full test suite with pytest."""
    print("Running full test suite...")
    print("=" * 80)
    
    # Run pytest with verbose output and coverage
    result = subprocess.run(
        [
            "python", "-m", "pytest", 
            "tests/",
            "-v",
            "--tb=short",
            "--maxfail=5",  # Stop after 5 failures to avoid overwhelming output
            f"--cov=src/fraud_detection",
            "--cov-report=term-missing",
            "--cov-report=json:scripts/reorganization/coverage_report.json"
        ],
        capture_output=True,
        text=True
    )
    
    return result

def parse_test_results(result):
    """Parse pytest output to extract test statistics."""
    output = result.stdout + result.stderr
    
    # Extract test counts from pytest output
    stats = {
        "return_code": result.returncode,
        "passed": 0,
        "failed": 0,
        "skipped": 0,
        "errors": 0,
        "warnings": 0
    }
    
    # Parse the summary line
    for line in output.split('\n'):
        if 'passed' in line.lower() or 'failed' in line.lower():
            # Look for patterns like "5 passed, 2 failed"
            parts = line.split()
            for i, part in enumerate(parts):
                if i > 0:
                    try:
                        count = int(parts[i-1])
                        if 'passed' in part:
                            stats['passed'] = count
                        elif 'failed' in part:
                            stats['failed'] = count
                        elif 'skipped' in part:
                            stats['skipped'] = count
                        elif 'error' in part:
                            stats['errors'] = count
                    except (ValueError, IndexError):
                        pass
    
    return stats

def compare_with_baseline(current_stats, baseline):
    """Compare current test results with baseline."""
    if not baseline:
        print("\n⚠️  No baseline found - this will serve as the new baseline")
        return True
    
    print("\n" + "=" * 80)
    print("COMPARISON WITH BASELINE")
    print("=" * 80)
    
    # For now, we just check if tests can be discovered and run
    # The baseline was just test discovery, so we're comparing success
    baseline_success = baseline.get('test_discovery_successful', False)
    current_success = current_stats['return_code'] in [0, 5]  # 0 = all passed, 5 = no tests collected
    
    print(f"Baseline test discovery: {'✓ Success' if baseline_success else '✗ Failed'}")
    print(f"Current test execution:  {'✓ Success' if current_success else '✗ Failed'}")
    
    if current_stats['passed'] > 0:
        print(f"\n✓ Tests passed: {current_stats['passed']}")
    if current_stats['failed'] > 0:
        print(f"✗ Tests failed: {current_stats['failed']}")
    if current_stats['skipped'] > 0:
        print(f"⊘ Tests skipped: {current_stats['skipped']}")
    if current_stats['errors'] > 0:
        print(f"✗ Test errors: {current_stats['errors']}")
    
    return current_success

def save_results(result, stats):
    """Save test results to file."""
    output_dir = Path("scripts/reorganization")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results = {
        "timestamp": datetime.datetime.now().isoformat(),
        "return_code": result.returncode,
        "statistics": stats,
        "stdout": result.stdout,
        "stderr": result.stderr
    }
    
    results_file = output_dir / "full_test_results.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\nTest results saved to: {results_file}")
    
    # Also save a human-readable report
    report_file = output_dir / "TEST_SUITE_REPORT.md"
    with open(report_file, "w") as f:
        f.write("# Full Test Suite Report\n\n")
        f.write(f"**Timestamp:** {results['timestamp']}\n\n")
        f.write(f"**Return Code:** {result.returncode}\n\n")
        f.write("## Test Statistics\n\n")
        f.write(f"- Passed: {stats['passed']}\n")
        f.write(f"- Failed: {stats['failed']}\n")
        f.write(f"- Skipped: {stats['skipped']}\n")
        f.write(f"- Errors: {stats['errors']}\n\n")
        f.write("## Test Output\n\n")
        f.write("```\n")
        f.write(result.stdout)
        if result.stderr:
            f.write("\n\nSTDERR:\n")
            f.write(result.stderr)
        f.write("\n```\n")
    
    print(f"Test report saved to: {report_file}")
    
    return results_file

def main():
    """Main execution function."""
    print("Full Test Suite Validation")
    print("=" * 80)
    
    # Load baseline
    baseline = load_baseline()
    if baseline:
        print(f"✓ Baseline loaded from: scripts/reorganization/baseline_test_discovery.json")
    else:
        print("⚠️  No baseline found - running without comparison")
    
    print()
    
    # Run tests
    result = run_test_suite()
    
    # Parse results
    stats = parse_test_results(result)
    
    # Print output
    print("\n" + "=" * 80)
    print("TEST OUTPUT")
    print("=" * 80)
    print(result.stdout)
    if result.stderr:
        print("\nSTDERR:")
        print(result.stderr)
    
    # Compare with baseline
    success = compare_with_baseline(stats, baseline)
    
    # Save results
    save_results(result, stats)
    
    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    if result.returncode == 0:
        print("✓ All tests passed!")
        return 0
    elif result.returncode == 5:
        print("⚠️  No tests collected - check test discovery")
        return 1
    else:
        print(f"✗ Tests failed with return code: {result.returncode}")
        if stats['failed'] > 0:
            print(f"  {stats['failed']} test(s) failed")
        if stats['errors'] > 0:
            print(f"  {stats['errors']} test(s) had errors")
        return 1

if __name__ == "__main__":
    sys.exit(main())
