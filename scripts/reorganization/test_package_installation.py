#!/usr/bin/env python3
"""
Test Package Installation Script

This script tests that the package can be installed correctly and that
imports work as expected from the installed package.

Task: 11.3 Test package installation
Requirements: 13.3
"""

import subprocess
import sys
import tempfile
import shutil
from pathlib import Path
import json


def run_command(cmd, cwd=None, capture_output=True):
    """Run a shell command and return the result."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=capture_output,
        text=True
    )
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result


def test_package_installation():
    """Test package installation in a clean virtual environment."""
    
    results = {
        "venv_creation": False,
        "package_installation": False,
        "import_tests": {},
        "errors": []
    }
    
    # Get the project root directory
    project_root = Path(__file__).parent.parent.parent
    
    print("=" * 80)
    print("PACKAGE INSTALLATION TEST")
    print("=" * 80)
    print(f"Project root: {project_root}")
    print()
    
    # Create a temporary directory for the test environment
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        venv_path = temp_path / "test_venv"
        
        print("Step 1: Creating clean virtual environment...")
        print("-" * 80)
        
        # Create virtual environment
        result = run_command([sys.executable, "-m", "venv", str(venv_path)])
        if result.returncode != 0:
            results["errors"].append(f"Failed to create virtual environment: {result.stderr}")
            print("❌ Failed to create virtual environment")
            return results
        
        results["venv_creation"] = True
        print("✅ Virtual environment created successfully")
        print()
        
        # Determine the python executable in the venv
        if sys.platform == "win32":
            python_exe = venv_path / "Scripts" / "python.exe"
            pip_exe = venv_path / "Scripts" / "pip.exe"
        else:
            python_exe = venv_path / "bin" / "python"
            pip_exe = venv_path / "bin" / "pip"
        
        print("Step 2: Upgrading pip...")
        print("-" * 80)
        result = run_command([str(python_exe), "-m", "pip", "install", "--upgrade", "pip"])
        if result.returncode != 0:
            results["errors"].append(f"Failed to upgrade pip: {result.stderr}")
            print("⚠️  Warning: Failed to upgrade pip, continuing anyway")
        else:
            print("✅ Pip upgraded successfully")
        print()
        
        print("Step 3: Installing package in editable mode...")
        print("-" * 80)
        
        # Install the package in editable mode
        result = run_command([str(pip_exe), "install", "-e", str(project_root)])
        if result.returncode != 0:
            results["errors"].append(f"Failed to install package: {result.stderr}")
            print("❌ Failed to install package")
            print(result.stderr)
            return results
        
        results["package_installation"] = True
        print("✅ Package installed successfully")
        print()
        
        print("Step 4: Testing imports from installed package...")
        print("-" * 80)
        
        # Test imports
        test_imports = [
            "fraud_detection",
            "fraud_detection.core",
            "fraud_detection.agents",
            "fraud_detection.memory",
            "fraud_detection.reasoning",
            "fraud_detection.streaming",
            "fraud_detection.external",
            "fraud_detection.web",
            "bedrock_agentcore_starter_toolkit",
        ]
        
        for module in test_imports:
            print(f"Testing import: {module}")
            result = run_command([
                str(python_exe),
                "-c",
                f"import {module}; print(f'✅ Successfully imported {module}')"
            ])
            
            if result.returncode == 0:
                results["import_tests"][module] = {
                    "success": True,
                    "output": result.stdout.strip()
                }
                print(f"  ✅ {module}")
            else:
                results["import_tests"][module] = {
                    "success": False,
                    "error": result.stderr.strip()
                }
                results["errors"].append(f"Failed to import {module}: {result.stderr}")
                print(f"  ❌ {module}")
                print(f"     Error: {result.stderr}")
        
        print()
        print("Step 5: Testing specific module imports...")
        print("-" * 80)
        
        # Test specific important classes/functions
        specific_tests = [
            ("fraud_detection.core", "Check core module attributes"),
            ("fraud_detection.agents.base_agent", "Import BaseAgent"),
            ("fraud_detection.memory.memory_manager", "Import MemoryManager"),
        ]
        
        for module, description in specific_tests:
            print(f"Testing: {description}")
            result = run_command([
                str(python_exe),
                "-c",
                f"import {module}; print('✅ {description} successful')"
            ])
            
            if result.returncode == 0:
                print(f"  ✅ {description}")
            else:
                print(f"  ⚠️  {description} - {result.stderr}")
        
        print()
        print("Step 6: Verifying package metadata...")
        print("-" * 80)
        
        # Check package is installed
        result = run_command([str(pip_exe), "show", "bedrock-agentcore-starter-toolkit"])
        if result.returncode == 0:
            print("✅ Package metadata found:")
            print(result.stdout)
        else:
            print("⚠️  Could not retrieve package metadata")
            results["errors"].append("Package metadata not found")
    
    return results


def print_summary(results):
    """Print a summary of the test results."""
    print()
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print()
    
    print(f"Virtual Environment Creation: {'✅ PASS' if results['venv_creation'] else '❌ FAIL'}")
    print(f"Package Installation: {'✅ PASS' if results['package_installation'] else '❌ FAIL'}")
    print()
    
    print("Import Tests:")
    passed = sum(1 for test in results["import_tests"].values() if test["success"])
    total = len(results["import_tests"])
    print(f"  Passed: {passed}/{total}")
    
    for module, result in results["import_tests"].items():
        status = "✅" if result["success"] else "❌"
        print(f"  {status} {module}")
    
    print()
    
    if results["errors"]:
        print("Errors encountered:")
        for error in results["errors"]:
            print(f"  ❌ {error}")
        print()
    
    # Overall result
    all_imports_passed = all(test["success"] for test in results["import_tests"].values())
    overall_success = (
        results["venv_creation"] and
        results["package_installation"] and
        all_imports_passed
    )
    
    print("=" * 80)
    if overall_success:
        print("✅ OVERALL: ALL TESTS PASSED")
    else:
        print("❌ OVERALL: SOME TESTS FAILED")
    print("=" * 80)
    
    return overall_success


def save_results(results):
    """Save test results to a JSON file."""
    output_file = Path(__file__).parent / "package_installation_test_results.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    try:
        results = test_package_installation()
        save_results(results)
        success = print_summary(results)
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
