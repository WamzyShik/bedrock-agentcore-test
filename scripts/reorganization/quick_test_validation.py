#!/usr/bin/env python3
"""
Quick Test Suite Validation

Tests specific directories to identify issues and validate the reorganization.
"""

import subprocess
import sys
from pathlib import Path


def test_directory(test_path: str, description: str) -> dict:
    """Test a specific directory."""
    print(f"\nTesting: {description}")
    print(f"Path: {test_path}")
    print("-" * 60)
    
    try:
        result = subprocess.run(
            ["python", "-m", "pytest", test_path, "--collect-only", "-q"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # Count tests
        test_count = result.stdout.count(" test")
        
        status = "✅ PASS" if result.returncode in [0, 5] else "❌ FAIL"
        print(f"Status: {status}")
        print(f"Return Code: {result.returncode}")
        print(f"Tests Found: {test_count}")
        
        if result.stderr:
            print(f"Errors: {result.stderr[:200]}")
        
        return {
            "path": test_path,
            "description": description,
            "success": result.returncode in [0, 5],
            "return_code": result.returncode,
            "test_count": test_count,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.TimeoutExpired:
        print(f"Status: ⚠️ TIMEOUT")
        return {
            "path": test_path,
            "description": description,
            "success": False,
            "return_code": -1,
            "test_count": 0,
            "error": "Timeout after 10 seconds"
        }
    except Exception as e:
        print(f"Status: ❌ ERROR - {str(e)}")
        return {
            "path": test_path,
            "description": description,
            "success": False,
            "return_code": -1,
            "test_count": 0,
            "error": str(e)
        }


def main():
    """Run validation on test directories."""
    print("=" * 80)
    print("QUICK TEST SUITE VALIDATION")
    print("=" * 80)
    
    # Test directories to validate
    test_dirs = [
        ("tests/cli/", "CLI Tests"),
        ("tests/services/", "Services Tests"),
        ("tests/utils/", "Utils Tests"),
        ("tests/unit/", "Unit Tests"),
        ("tests/integration/", "Integration Tests"),
        ("tests/fixtures/", "Fixtures"),
    ]
    
    results = []
    for test_path, description in test_dirs:
        if Path(test_path).exists():
            result = test_directory(test_path, description)
            results.append(result)
        else:
            print(f"\n⚠️ Skipping {description} - path does not exist: {test_path}")
    
    # Summary
    print("\n" + "=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    
    total_tests = sum(r.get('test_count', 0) for r in results)
    successful = sum(1 for r in results if r.get('success', False))
    failed = len(results) - successful
    
    print(f"\nDirectories Tested: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total Tests Discovered: {total_tests}")
    
    if failed > 0:
        print("\n❌ Failed Directories:")
        for r in results:
            if not r.get('success', False):
                print(f"  - {r['description']} ({r['path']})")
                if 'error' in r:
                    print(f"    Error: {r['error']}")
    
    # Test discovery issues
    print("\n" + "=" * 80)
    print("TEST DISCOVERY ISSUES")
    print("=" * 80)
    
    issues_found = False
    for r in results:
        if 'stderr' in r and r['stderr']:
            if 'error' in r['stderr'].lower() or 'import' in r['stderr'].lower():
                issues_found = True
                print(f"\n{r['description']} ({r['path']}):")
                print(r['stderr'][:500])
    
    if not issues_found:
        print("\n✅ No import or discovery issues detected")
    
    # Recommendations
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    
    if failed == 0 and total_tests > 0:
        print("\n✅ All test directories are working correctly")
        print("✅ Test discovery is functioning properly")
        print("✅ Ready to run full test suite")
        print("\nNext steps:")
        print("  1. Run full test suite: python -m pytest tests/ -v")
        print("  2. Check for any test failures")
        print("  3. Update documentation with test results")
    else:
        print("\n⚠️ Issues detected:")
        if total_tests == 0:
            print("  - No tests were discovered")
            print("  - Check pytest configuration in pyproject.toml")
            print("  - Verify test file naming (test_*.py or *_test.py)")
        if failed > 0:
            print("  - Some directories failed test discovery")
            print("  - Check import statements in failing tests")
            print("  - Verify module paths are correct")
            print("  - Run: python scripts/reorganization/scan_dependencies.py")
    
    print("\n" + "=" * 80)
    
    return 0 if failed == 0 and total_tests > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
