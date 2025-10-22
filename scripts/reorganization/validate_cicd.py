#!/usr/bin/env python3
"""
Validate CI/CD Configuration Script

This script validates that the CI/CD pipeline configuration is correct
and all referenced paths and scripts exist.

Task: 11.5 Test CI/CD pipeline
Requirements: 15.4, 15.6
"""

import json
import yaml
from pathlib import Path
from typing import Dict, List, Any


def load_workflow(workflow_path: Path) -> Dict[str, Any]:
    """Load GitHub Actions workflow file."""
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading workflow: {e}")
        return {}


def validate_paths(workflow: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that all paths referenced in the workflow exist."""
    results = {
        "paths_checked": 0,
        "paths_valid": 0,
        "paths_missing": [],
        "errors": []
    }
    
    # Check environment variables for paths
    env_vars = workflow.get('env', {})
    path_vars = {
        'SRC_PATH': env_vars.get('SRC_PATH', 'src'),
        'TESTS_PATH': env_vars.get('TESTS_PATH', 'tests'),
        'INFRASTRUCTURE_PATH': env_vars.get('INFRASTRUCTURE_PATH', 'infrastructure'),
        'SCRIPTS_PATH': env_vars.get('SCRIPTS_PATH', 'scripts'),
        'EXAMPLES_PATH': env_vars.get('EXAMPLES_PATH', 'examples'),
    }
    
    print("Checking environment path variables...")
    print("-" * 80)
    
    for var_name, path_value in path_vars.items():
        results["paths_checked"] += 1
        path = Path(path_value)
        
        if path.exists():
            results["paths_valid"] += 1
            print(f"✅ {var_name}: {path_value}")
        else:
            results["paths_missing"].append(f"{var_name}: {path_value}")
            print(f"❌ {var_name}: {path_value} (not found)")
    
    print()
    
    # Check specific script paths mentioned in workflow
    print("Checking referenced scripts...")
    print("-" * 80)
    
    script_paths = [
        "infrastructure/aws/deployment/deploy_full_infrastructure.py",
        "infrastructure/aws/deployment/deploy_blue_green.sh",
        "infrastructure/aws/deployment/rollback_deployment.sh",
    ]
    
    for script_path in script_paths:
        results["paths_checked"] += 1
        path = Path(script_path)
        
        if path.exists():
            results["paths_valid"] += 1
            print(f"✅ {script_path}")
        else:
            results["paths_missing"].append(script_path)
            print(f"⚠️  {script_path} (not found - may need to be created)")
    
    print()
    
    return results


def validate_test_commands(workflow: Dict[str, Any]) -> Dict[str, Any]:
    """Validate test commands in the workflow."""
    results = {
        "test_jobs": [],
        "valid": True,
        "errors": []
    }
    
    print("Checking test job configurations...")
    print("-" * 80)
    
    jobs = workflow.get('jobs', {})
    
    # Check test job
    if 'test' in jobs:
        test_job = jobs['test']
        steps = test_job.get('steps', [])
        
        for step in steps:
            if 'Run unit tests' in step.get('name', ''):
                run_cmd = step.get('run', '')
                if 'pytest' in run_cmd and ('tests/' in run_cmd or 'TESTS_PATH' in run_cmd):
                    print(f"✅ Test command uses correct path (tests/ or $TESTS_PATH)")
                    results["test_jobs"].append("unit_tests")
                else:
                    print(f"⚠️  Test command may need updating")
                    results["errors"].append("Test command doesn't use tests/ path")
    
    # Check lint job
    if 'lint' in jobs:
        print(f"✅ Lint job configured")
        results["test_jobs"].append("lint")
    
    # Check security job
    if 'security' in jobs:
        print(f"✅ Security scan job configured")
        results["test_jobs"].append("security")
    
    print()
    
    return results


def validate_deployment_jobs(workflow: Dict[str, Any]) -> Dict[str, Any]:
    """Validate deployment job configurations."""
    results = {
        "deployment_jobs": [],
        "valid": True,
        "errors": []
    }
    
    print("Checking deployment job configurations...")
    print("-" * 80)
    
    jobs = workflow.get('jobs', {})
    
    deployment_jobs = ['deploy-dev', 'deploy-staging', 'deploy-prod']
    
    for job_name in deployment_jobs:
        if job_name in jobs:
            job = jobs[job_name]
            
            # Check if job has environment configured
            if 'environment' in job:
                env_name = job['environment'].get('name', 'unknown')
                print(f"✅ {job_name}: environment={env_name}")
                results["deployment_jobs"].append(job_name)
            else:
                print(f"⚠️  {job_name}: no environment configured")
                results["errors"].append(f"{job_name} missing environment")
        else:
            print(f"⚠️  {job_name}: not found in workflow")
    
    print()
    
    return results


def check_requirements_file() -> Dict[str, Any]:
    """Check if requirements.txt or pyproject.toml exists and is valid."""
    results = {
        "exists": False,
        "valid": False,
        "package_count": 0,
        "file_type": None,
        "errors": []
    }
    
    print("Checking dependency configuration...")
    print("-" * 80)
    
    # Check for pyproject.toml first (modern Python projects)
    pyproject_file = Path("pyproject.toml")
    req_file = Path("requirements.txt")
    
    if pyproject_file.exists():
        results["exists"] = True
        results["file_type"] = "pyproject.toml"
        results["valid"] = True
        print(f"✅ pyproject.toml found (modern Python packaging)")
        
        try:
            import tomli
            with open(pyproject_file, 'rb') as f:
                data = tomli.load(f)
                if 'project' in data and 'dependencies' in data['project']:
                    deps = data['project']['dependencies']
                    results["package_count"] = len(deps)
                    print(f"✅ Contains {len(deps)} package dependencies")
        except ImportError:
            print(f"⚠️  tomli not installed, cannot parse pyproject.toml")
        except Exception as e:
            print(f"⚠️  Could not parse dependencies: {e}")
    
    elif req_file.exists():
        results["exists"] = True
        results["file_type"] = "requirements.txt"
        print(f"✅ requirements.txt found")
        
        try:
            with open(req_file, 'r') as f:
                lines = f.readlines()
                packages = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
                results["package_count"] = len(packages)
                results["valid"] = True
                print(f"✅ Contains {len(packages)} package requirements")
        except Exception as e:
            results["errors"].append(f"Error reading requirements.txt: {e}")
            print(f"❌ Error reading file: {e}")
    else:
        results["errors"].append("No dependency file found (requirements.txt or pyproject.toml)")
        print(f"❌ No dependency file found")
    
    print()
    
    return results


def validate_cicd():
    """Main validation function."""
    print("=" * 80)
    print("CI/CD CONFIGURATION VALIDATION")
    print("=" * 80)
    print()
    
    workflow_path = Path(".github/workflows/ci-cd.yml")
    
    if not workflow_path.exists():
        print(f"❌ Workflow file not found: {workflow_path}")
        return {
            "success": False,
            "error": "Workflow file not found"
        }
    
    print(f"✅ Workflow file found: {workflow_path}")
    print()
    
    # Load workflow
    workflow = load_workflow(workflow_path)
    
    if not workflow:
        return {
            "success": False,
            "error": "Failed to load workflow"
        }
    
    # Run validations
    path_results = validate_paths(workflow)
    test_results = validate_test_commands(workflow)
    deploy_results = validate_deployment_jobs(workflow)
    req_results = check_requirements_file()
    
    # Summary
    print("=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print()
    
    print(f"Paths checked: {path_results['paths_checked']}")
    print(f"Paths valid: {path_results['paths_valid']}")
    
    if path_results['paths_missing']:
        print(f"\nMissing paths:")
        for path in path_results['paths_missing']:
            print(f"  ⚠️  {path}")
    
    print(f"\nTest jobs configured: {len(test_results['test_jobs'])}")
    for job in test_results['test_jobs']:
        print(f"  ✅ {job}")
    
    print(f"\nDeployment jobs configured: {len(deploy_results['deployment_jobs'])}")
    for job in deploy_results['deployment_jobs']:
        print(f"  ✅ {job}")
    
    print(f"\nRequirements file: {'✅ Valid' if req_results['valid'] else '❌ Invalid'}")
    
    # Overall result
    all_errors = (
        path_results['errors'] +
        test_results['errors'] +
        deploy_results['errors'] +
        req_results['errors']
    )
    
    print()
    print("=" * 80)
    
    if not all_errors and path_results['paths_valid'] >= 4:  # At least 4 of 5 paths should exist
        print("✅ OVERALL: CI/CD CONFIGURATION IS VALID")
        print("The workflow is properly configured for the reorganized structure.")
        success = True
    else:
        print("⚠️  OVERALL: CI/CD CONFIGURATION HAS SOME ISSUES")
        print("Some paths or configurations may need attention.")
        if all_errors:
            print("\nErrors:")
            for error in all_errors:
                print(f"  ❌ {error}")
        success = False
    
    print("=" * 80)
    
    results = {
        "success": success,
        "workflow_file": str(workflow_path),
        "paths": path_results,
        "tests": test_results,
        "deployments": deploy_results,
        "requirements": req_results,
        "errors": all_errors
    }
    
    return results


def save_results(results: Dict[str, Any]):
    """Save validation results to JSON file."""
    output_file = Path(__file__).parent / "cicd_validation_results.json"
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    import sys
    
    try:
        results = validate_cicd()
        save_results(results)
        sys.exit(0 if results["success"] else 1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
