#!/usr/bin/env python3
"""
Import Validation Script

This script validates that all modules in src/fraud_detection/ can be imported
successfully and checks for missing dependencies.

Usage:
    python scripts/reorganization/validate_imports.py
"""

import importlib
import importlib.util
import sys
from pathlib import Path
from typing import List, Dict, Tuple
import json
from datetime import datetime


class ImportValidator:
    """Validates imports across the reorganized codebase."""
    
    def __init__(self, src_root: Path):
        self.src_root = src_root
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "total_modules": 0,
            "successful_imports": 0,
            "failed_imports": 0,
            "modules": {},
            "summary": {}
        }
    
    def discover_modules(self) -> List[str]:
        """Discover all Python modules in src/fraud_detection/."""
        modules = []
        fraud_detection_path = self.src_root / "fraud_detection"
        
        if not fraud_detection_path.exists():
            print(f"❌ Error: {fraud_detection_path} does not exist")
            return modules
        
        for py_file in fraud_detection_path.rglob("*.py"):
            # Skip __pycache__ and other non-module files
            if "__pycache__" in str(py_file):
                continue
            
            # Convert file path to module name
            relative_path = py_file.relative_to(self.src_root)
            module_parts = list(relative_path.parts[:-1]) + [relative_path.stem]
            
            # Skip __init__ files for now (we'll import the package instead)
            if module_parts[-1] == "__init__":
                module_parts = module_parts[:-1]
            
            if module_parts:  # Only add non-empty module paths
                module_name = ".".join(module_parts)
                modules.append(module_name)
        
        return sorted(set(modules))  # Remove duplicates and sort
    
    def validate_import(self, module_name: str) -> Tuple[bool, str]:
        """
        Attempt to import a module and return success status and error message.
        
        Returns:
            Tuple of (success: bool, error_message: str)
        """
        try:
            # Try to import the module
            importlib.import_module(module_name)
            return True, ""
        except ImportError as e:
            return False, f"ImportError: {str(e)}"
        except Exception as e:
            return False, f"{type(e).__name__}: {str(e)}"
    
    def validate_all_imports(self) -> Dict:
        """Validate all discovered modules."""
        print("🔍 Discovering modules...")
        modules = self.discover_modules()
        
        self.results["total_modules"] = len(modules)
        print(f"📦 Found {len(modules)} modules to validate\n")
        
        print("🧪 Validating imports...")
        print("-" * 80)
        
        for module_name in modules:
            success, error = self.validate_import(module_name)
            
            self.results["modules"][module_name] = {
                "success": success,
                "error": error
            }
            
            if success:
                self.results["successful_imports"] += 1
                print(f"✅ {module_name}")
            else:
                self.results["failed_imports"] += 1
                print(f"❌ {module_name}")
                print(f"   Error: {error}")
        
        print("-" * 80)
        return self.results
    
    def generate_report(self) -> str:
        """Generate a human-readable validation report."""
        report_lines = [
            "=" * 80,
            "IMPORT VALIDATION REPORT",
            "=" * 80,
            f"Timestamp: {self.results['timestamp']}",
            f"Total Modules: {self.results['total_modules']}",
            f"Successful Imports: {self.results['successful_imports']}",
            f"Failed Imports: {self.results['failed_imports']}",
            ""
        ]
        
        if self.results['failed_imports'] > 0:
            report_lines.extend([
                "FAILED IMPORTS:",
                "-" * 80
            ])
            
            for module_name, result in self.results['modules'].items():
                if not result['success']:
                    report_lines.append(f"\n❌ {module_name}")
                    report_lines.append(f"   {result['error']}")
            
            report_lines.append("")
        
        # Summary
        success_rate = (self.results['successful_imports'] / self.results['total_modules'] * 100) if self.results['total_modules'] > 0 else 0
        
        report_lines.extend([
            "SUMMARY:",
            "-" * 80,
            f"Success Rate: {success_rate:.1f}%",
            ""
        ])
        
        if self.results['failed_imports'] == 0:
            report_lines.append("✅ All imports validated successfully!")
        else:
            report_lines.append(f"⚠️  {self.results['failed_imports']} import(s) failed validation")
        
        report_lines.append("=" * 80)
        
        return "\n".join(report_lines)
    
    def save_report(self, output_path: Path):
        """Save validation report to file."""
        report = self.generate_report()
        
        # Save text report with UTF-8 encoding
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        # Save JSON report
        json_path = output_path.with_suffix('.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n📄 Report saved to: {output_path}")
        print(f"📄 JSON report saved to: {json_path}")


def main():
    """Main execution function."""
    # Get the project root (assuming script is in scripts/reorganization/)
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent.parent
    src_root = project_root / "src"
    
    print("=" * 80)
    print("IMPORT VALIDATION SCRIPT")
    print("=" * 80)
    print(f"Project Root: {project_root}")
    print(f"Source Root: {src_root}")
    print()
    
    # Add src to Python path
    if str(src_root) not in sys.path:
        sys.path.insert(0, str(src_root))
        print(f"✅ Added {src_root} to Python path\n")
    
    # Create validator and run validation
    validator = ImportValidator(src_root)
    results = validator.validate_all_imports()
    
    # Generate and display report
    print("\n")
    report = validator.generate_report()
    print(report)
    
    # Save report
    output_path = script_path.parent / "import_validation_report.txt"
    validator.save_report(output_path)
    
    # Exit with appropriate code
    if results['failed_imports'] > 0:
        print("\n⚠️  Validation completed with errors")
        sys.exit(1)
    else:
        print("\n✅ Validation completed successfully")
        sys.exit(0)


if __name__ == "__main__":
    main()
