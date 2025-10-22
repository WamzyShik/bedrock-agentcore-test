#!/usr/bin/env python3
"""
Test Package Imports in Current Environment

This script tests that the fraud_detection package can be imported correctly
in the current environment where dependencies are already installed.

Task: 11.3 Test package installation
Requirements: 13.3
"""

import sys
import importlib
import json
from pathlib import Path


def test_imports():
    """Test importing all fraud_detection modules."""
    
    results = {
        "import_tests": {},
        "module_attributes": {},
        "errors": []
    }
    
    print("=" * 80)
    print("FRAUD DETECTION PACKAGE IMPORT TEST")
    print("=" * 80)
    print()
    
    # Test main package imports
    test_modules = [
        "fraud_detection",
        "fraud_detection.core",
        "fraud_detection.agents",
        "fraud_detection.agents.base_agent",
        "fraud_detection.agents.coordination",
        "fraud_detection.agents.specialized",
        "fraud_detection.agents.bedrock",
        "fraud_detection.memory",
        "fraud_detection.memory.memory_manager",
        "fraud_detection.memory.context_manager",
        "fraud_detection.reasoning",
        "fraud_detection.reasoning.adaptive_reasoning",
        "fraud_detection.streaming",
        "fraud_detection.external",
        "fraud_detection.web",
        "fraud_detection.web.dashboards",
        "fraud_detection.web.api",
    ]
    
    print("Testing module imports...")
    print("-" * 80)
    
    for module_name in test_modules:
        try:
            module = importlib.import_module(module_name)
            results["import_tests"][module_name] = {
                "success": True,
                "path": str(getattr(module, "__file__", "N/A"))
            }
            print(f"✅ {module_name}")
            
            # Check for key attributes
            if hasattr(module, "__all__"):
                results["module_attributes"][module_name] = {
                    "__all__": module.__all__
                }
            
        except Exception as e:
            results["import_tests"][module_name] = {
                "success": False,
                "error": str(e)
            }
            results["errors"].append(f"Failed to import {module_name}: {e}")
            print(f"❌ {module_name}: {e}")
    
    print()
    print("Testing specific class imports...")
    print("-" * 80)
    
    # Test specific important classes
    specific_imports = [
        ("fraud_detection.agents.base_agent", "BaseAgent"),
        ("fraud_detection.memory.memory_manager", "MemoryManager"),
        ("fraud_detection.memory.context_manager", "ContextManager"),
    ]
    
    for module_name, class_name in specific_imports:
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, class_name):
                print(f"✅ {module_name}.{class_name}")
                results["import_tests"][f"{module_name}.{class_name}"] = {
                    "success": True
                }
            else:
                print(f"⚠️  {module_name}.{class_name} - attribute not found")
                results["import_tests"][f"{module_name}.{class_name}"] = {
                    "success": False,
                    "error": "Attribute not found"
                }
        except Exception as e:
            print(f"❌ {module_name}.{class_name}: {e}")
            results["import_tests"][f"{module_name}.{class_name}"] = {
                "success": False,
                "error": str(e)
            }
    
    print()
    print("Checking package structure...")
    print("-" * 80)
    
    # Check that src/fraud_detection exists and has proper structure
    src_path = Path("src/fraud_detection")
    if src_path.exists():
        print(f"✅ Package directory exists: {src_path}")
        
        # Check for __init__.py files
        init_files = list(src_path.rglob("__init__.py"))
        print(f"✅ Found {len(init_files)} __init__.py files")
        
        # List subdirectories
        subdirs = [d.name for d in src_path.iterdir() if d.is_dir() and not d.name.startswith("__")]
        print(f"✅ Package subdirectories: {', '.join(subdirs)}")
        
        results["package_structure"] = {
            "exists": True,
            "init_files_count": len(init_files),
            "subdirectories": subdirs
        }
    else:
        print(f"❌ Package directory not found: {src_path}")
        results["package_structure"] = {
            "exists": False
        }
        results["errors"].append("Package directory not found")
    
    return results


def print_summary(results):
    """Print a summary of the test results."""
    print()
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print()
    
    # Count successes
    passed = sum(1 for test in results["import_tests"].values() if test.get("success", False))
    total = len(results["import_tests"])
    
    print(f"Import Tests: {passed}/{total} passed")
    print()
    
    if results["errors"]:
        print("Errors encountered:")
        for error in results["errors"]:
            print(f"  ❌ {error}")
        print()
    
    # Overall result
    all_passed = passed == total and not results["errors"]
    
    print("=" * 80)
    if all_passed:
        print("✅ OVERALL: ALL TESTS PASSED")
        print("The fraud_detection package is properly structured and importable.")
    else:
        print("⚠️  OVERALL: SOME TESTS FAILED")
        print(f"Success rate: {passed}/{total} ({100*passed//total if total > 0 else 0}%)")
    print("=" * 80)
    
    return all_passed


def save_results(results):
    """Save test results to a JSON file."""
    output_file = Path(__file__).parent / "current_env_import_test_results.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    try:
        results = test_imports()
        save_results(results)
        success = print_summary(results)
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
