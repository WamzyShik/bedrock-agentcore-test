#!/usr/bin/env python3
"""
Fix Example Imports Script

This script fixes src. imports in example files to use the correct fraud_detection imports.
"""

import re
from pathlib import Path
from typing import List, Tuple


def fix_imports_in_file(file_path: Path) -> Tuple[bool, List[str]]:
    """Fix imports in a single file."""
    changes = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix src.fraud_detection imports
        patterns = [
            (r'from src\.fraud_detection\.agents\.specialized\.([a-z_]+) import',
             r'from fraud_detection.agents.specialized.specialized_agents.\1 import'),
            (r'from src\.fraud_detection\.agents\.base_agent import',
             r'from fraud_detection.agents.specialized.specialized_agents.base_agent import'),
            (r'from src\.fraud_detection\.core\.models import',
             r'from fraud_detection.memory.models import'),
            (r'from src\.fraud_detection\.memory\.([a-z_]+) import',
             r'from fraud_detection.memory.\1 import'),
            (r'from src\.fraud_detection\.reasoning\.([a-z_]+) import',
             r'from fraud_detection.reasoning.\1 import'),
            (r'from src\.fraud_detection\.streaming\.([a-z_]+) import',
             r'from fraud_detection.streaming.\1 import'),
            (r'from src\.fraud_detection\.external\.([a-z_]+) import',
             r'from fraud_detection.external.\1 import'),
            (r'from src\.fraud_detection\.core\.([a-z_]+) import',
             r'from fraud_detection.core.\1 import'),
        ]
        
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                changes.append(f"Fixed: {pattern}")
                content = new_content
        
        # Write back if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes
        
        return False, []
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []


def fix_all_examples():
    """Fix imports in all example files."""
    examples_dir = Path("examples")
    
    print("=" * 80)
    print("FIXING EXAMPLE IMPORTS")
    print("=" * 80)
    print()
    
    example_files = list(examples_dir.rglob("*.py"))
    example_files = [f for f in example_files if "__pycache__" not in str(f)]
    
    print(f"Found {len(example_files)} example files")
    print()
    
    fixed_count = 0
    
    for file_path in sorted(example_files):
        changed, changes = fix_imports_in_file(file_path)
        
        # Get relative path safely
        try:
            rel_path = file_path.relative_to(Path.cwd())
        except ValueError:
            rel_path = file_path
        
        if changed:
            fixed_count += 1
            print(f"✅ Fixed: {rel_path}")
            for change in changes:
                print(f"   {change}")
        else:
            print(f"⏭️  Skipped: {rel_path} (no changes needed)")
    
    print()
    print("=" * 80)
    print(f"Fixed {fixed_count}/{len(example_files)} files")
    print("=" * 80)


if __name__ == "__main__":
    fix_all_examples()
