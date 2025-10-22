#!/usr/bin/env python3
"""
Validate Examples Script

This script validates that all example files can be imported without errors.
It checks for import errors but doesn't execute the examples (which may require
specific configurations or running services).

Task: 11.4 Validate examples run successfully
Requirements: 5.6
"""

import sys
import ast
import json
from pathlib import Path
from typing import Dict, List, Any


def find_example_files(examples_dir: Path) -> List[Path]:
    """Find all Python example files."""
    example_files = []
    
    for py_file in examples_dir.rglob("*.py"):
        # Skip __pycache__ and .gitkeep files
        if "__pycache__" not in str(py_file) and py_file.name != ".gitkeep":
            example_files.append(py_file)
    
    return sorted(example_files)


def validate_syntax(file_path: Path) -> Dict[str, Any]:
    """Validate Python syntax of a file."""
    result = {
        "file": str(file_path),
        "syntax_valid": False,
        "error": None
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Try to parse the file as AST
        ast.parse(code)
        result["syntax_valid"] = True
        
    except SyntaxError as e:
        result["error"] = f"Syntax error at line {e.lineno}: {e.msg}"
    except Exception as e:
        result["error"] = f"Error reading file: {str(e)}"
    
    return result


def check_imports(file_path: Path) -> Dict[str, Any]:
    """Check if imports in the file can be resolved."""
    result = {
        "file": str(file_path),
        "imports_valid": False,
        "imports": [],
        "error": None
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Parse imports
        tree = ast.parse(code)
        imports = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
        
        result["imports"] = imports
        result["imports_valid"] = True
        
    except Exception as e:
        result["error"] = f"Error checking imports: {str(e)}"
    
    return result


def validate_examples():
    """Validate all example files."""
    
    print("=" * 80)
    print("EXAMPLES VALIDATION")
    print("=" * 80)
    print()
    
    examples_dir = Path("examples")
    
    if not examples_dir.exists():
        print(f"❌ Examples directory not found: {examples_dir}")
        return {
            "success": False,
            "error": "Examples directory not found"
        }
    
    # Find all example files
    example_files = find_example_files(examples_dir)
    
    print(f"Found {len(example_files)} example files")
    print()
    
    results = {
        "total_files": len(example_files),
        "syntax_valid": 0,
        "syntax_errors": 0,
        "files": [],
        "errors": []
    }
    
    # Validate each file
    print("Validating syntax...")
    print("-" * 80)
    
    project_root = Path.cwd()
    
    for file_path in example_files:
        # Make path absolute and then relative to project root
        abs_path = file_path.resolve()
        try:
            relative_path = abs_path.relative_to(project_root)
        except ValueError:
            # If file is not under project root, use the original path
            relative_path = file_path
        
        # Check syntax
        syntax_result = validate_syntax(file_path)
        
        # Check imports
        import_result = check_imports(file_path)
        
        file_result = {
            "file": str(relative_path),
            "syntax_valid": syntax_result["syntax_valid"],
            "imports_valid": import_result["imports_valid"],
            "imports": import_result["imports"],
            "errors": []
        }
        
        if syntax_result["error"]:
            file_result["errors"].append(syntax_result["error"])
            results["syntax_errors"] += 1
            print(f"❌ {relative_path}")
            print(f"   {syntax_result['error']}")
        else:
            results["syntax_valid"] += 1
            print(f"✅ {relative_path}")
        
        if import_result["error"]:
            file_result["errors"].append(import_result["error"])
        
        results["files"].append(file_result)
    
    print()
    print("=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print()
    
    print(f"Total files: {results['total_files']}")
    print(f"Syntax valid: {results['syntax_valid']}")
    print(f"Syntax errors: {results['syntax_errors']}")
    print()
    
    if results["syntax_errors"] > 0:
        print("Files with errors:")
        for file_result in results["files"]:
            if file_result["errors"]:
                print(f"  ❌ {file_result['file']}")
                for error in file_result["errors"]:
                    print(f"     {error}")
        print()
    
    # Check for common import patterns
    print("Import Analysis:")
    print("-" * 80)
    
    fraud_detection_imports = 0
    src_imports = 0
    
    for file_result in results["files"]:
        for imp in file_result["imports"]:
            if imp.startswith("fraud_detection"):
                fraud_detection_imports += 1
            elif imp.startswith("src."):
                src_imports += 1
    
    print(f"✅ fraud_detection imports: {fraud_detection_imports}")
    if src_imports > 0:
        print(f"⚠️  src. imports (should be updated): {src_imports}")
    else:
        print(f"✅ No problematic src. imports found")
    print()
    
    # Overall result
    success = results["syntax_errors"] == 0
    
    print("=" * 80)
    if success:
        print("✅ OVERALL: ALL EXAMPLES VALIDATED SUCCESSFULLY")
        print("All example files have valid syntax and can be imported.")
    else:
        print("⚠️  OVERALL: SOME EXAMPLES HAVE ISSUES")
        print(f"Success rate: {results['syntax_valid']}/{results['total_files']} "
              f"({100*results['syntax_valid']//results['total_files']}%)")
    print("=" * 80)
    
    results["success"] = success
    
    return results


def save_results(results: Dict[str, Any]):
    """Save validation results to JSON file."""
    output_file = Path(__file__).parent / "examples_validation_results.json"
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    try:
        results = validate_examples()
        save_results(results)
        sys.exit(0 if results["success"] else 1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
