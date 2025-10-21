# Scripts Directory

This directory contains utility scripts organized by purpose to support development, security, release management, and general utilities for the Fraud Detection System.

## Directory Structure

```
scripts/
├── security/          # Security scanning and audit scripts
├── release/           # Version management and release scripts
├── development/       # Development and testing utilities
├── utilities/         # General-purpose utility scripts
└── reorganization/    # Repository reorganization scripts
```

## Security Scripts (`security/`)

Scripts for security auditing and vulnerability scanning.

### `security_check.py`
Simple security check for Windows that checks for common security issues without external dependencies.

**Usage:**
```bash
python scripts/security/security_check.py
```

**Features:**
- Checks for exposed secrets and credentials
- Validates .gitignore configuration
- Reviews GitHub Actions workflow security
- Provides security recommendations

### `security_audit.py`
Comprehensive security audit script with detailed scanning capabilities.

**Usage:**
```bash
python scripts/security/security_audit.py
```

### `run_security_audit.py`
Comprehensive security, bug, and vulnerability testing that runs multiple security scanners and code quality checks.

**Usage:**
```bash
python scripts/security/run_security_audit.py
```

**Features:**
- Runs Bandit security vulnerability scan
- Checks for hardcoded passwords and API keys
- Generates detailed security reports
- Provides actionable recommendations

### `quick_security_check.sh`
Quick bash script for rapid security checks.

**Usage:**
```bash
bash scripts/security/quick_security_check.sh
```

## Release Scripts (`release/`)

Scripts for managing versions and preparing releases.

### `bump-version.py`
Automated version bumping for the project.

**Usage:**
```bash
python scripts/release/bump-version.py [major|minor|patch]
```

**Features:**
- Semantic versioning support
- Updates version across project files
- Creates git tags
- Generates changelog entries

### `prepare-release.py`
Prepares the project for a new release.

**Usage:**
```bash
python scripts/release/prepare-release.py
```

**Features:**
- Validates all tests pass
- Checks documentation is up to date
- Verifies no uncommitted changes
- Prepares release notes

### `validate-release.py`
Validates that a release is ready for deployment.

**Usage:**
```bash
python scripts/release/validate-release.py
```

**Features:**
- Runs comprehensive validation checks
- Verifies package integrity
- Checks dependencies
- Validates configuration files

## Development Scripts (`development/`)

Scripts to support development workflows.

### `run_all_tests.py`
Test runner that executes all test suites and generates comprehensive test reports.

**Usage:**
```bash
python scripts/development/run_all_tests.py
```

**Features:**
- Runs unit tests
- Runs integration tests
- Generates coverage reports
- Provides detailed test summaries

### `setup-branch-protection.sh`
Sets up branch protection rules for the repository.

**Usage:**
```bash
bash scripts/development/setup-branch-protection.sh
```

**Features:**
- Configures branch protection
- Sets up required reviews
- Enforces status checks

## Utility Scripts (`utilities/`)

General-purpose utility scripts for various tasks.

### `transaction_generator.py`
Generates realistic transaction data for testing.

**Usage:**
```bash
python scripts/utilities/transaction_generator.py
```

**Features:**
- Creates realistic transaction patterns
- Supports multiple currencies
- Generates both legitimate and fraudulent transactions
- Configurable data volume

**Dependencies:**
- faker
- requests

### `data_loader.py`
Utility for loading and managing test data.

**Usage:**
```python
from scripts.utilities.data_loader import DataLoader
loader = DataLoader()
data = loader.load_transactions()
```

### `currency_converter.py`
Currency conversion utility for multi-currency transaction processing.

**Usage:**
```python
from scripts.utilities.currency_converter import CurrencyConverter
converter = CurrencyConverter()
usd_amount = converter.convert(100, 'EUR', 'USD')
```

### `check_models.py`
Validates and checks AI model configurations.

**Usage:**
```bash
python scripts/utilities/check_models.py
```

**Features:**
- Verifies model availability
- Checks model configurations
- Validates model permissions

## Reorganization Scripts (`reorganization/`)

Scripts used for the repository reorganization project. These are primarily for historical reference and maintenance.

### Key Scripts:
- `scan_dependencies.py` - Analyzes module dependencies
- `update_imports.py` - Updates import statements after file moves
- `complete_reorganization.py` - Orchestrates the full reorganization
- `validate_test_suite.py` - Validates test suite after reorganization

## Common Dependencies

Most scripts require Python 3.8+ and may have additional dependencies:

```bash
# Install common dependencies
pip install -r requirements.txt
```

## Best Practices

1. **Always run from project root**: Scripts assume they're run from the repository root directory
2. **Check dependencies**: Review script headers for required dependencies
3. **Use virtual environment**: Run scripts in a Python virtual environment
4. **Review output**: Scripts provide detailed output - review for warnings or errors
5. **Test in development**: Test scripts in development environment before production use

## Contributing

When adding new scripts:

1. Place in appropriate subdirectory based on purpose
2. Include docstring with description and usage
3. Add entry to this README
4. Document dependencies
5. Include usage examples
6. Follow existing naming conventions

## Support

For issues or questions about scripts:
- Check script docstrings for detailed usage
- Review script output for error messages
- Consult project documentation in `docs/`
- Open an issue on GitHub
