# Test Changes Documentation

## Overview

This document outlines any test changes needed after the repository reorganization and provides guidance for running the test suite.

## Test Configuration Changes

### pytest Configuration (pyproject.toml)

✅ **Already Updated**

The pytest configuration in `pyproject.toml` has been updated to reflect the new structure:

```toml
[tool.pytest.ini_options]
testpaths = [
    "tests"
]
```

This ensures pytest looks for tests in the `tests/` directory, which is the correct location after reorganization.

## Test Structure

### Current Test Organization

```
tests/
├── cli/                    # CLI-related tests
├── fixtures/               # Shared test fixtures and data
├── integration/            # Integration tests
├── notebook/               # Notebook-related tests
├── operations/             # Operations tests
├── services/               # Service layer tests
├── unit/                   # Unit tests
│   ├── agents/            # Agent unit tests
│   ├── core/              # Core functionality tests
│   ├── external/          # External service tests
│   ├── memory/            # Memory system tests
│   ├── reasoning/         # Reasoning engine tests
│   └── streaming/         # Streaming tests
├── utils/                  # Utility tests
├── conftest.py            # Pytest configuration and fixtures
└── [root level tests]     # High-level integration/validation tests
```

## Test Discovery

### Working Test Directories

All test directories are functional and can discover tests correctly:

- ✅ `tests/cli/` - Fast discovery
- ✅ `tests/services/` - Fast discovery
- ✅ `tests/utils/` - Fast discovery
- ✅ `tests/unit/` - Functional (slower due to size)
- ✅ `tests/integration/` - Functional (slower due to complexity)

### Performance Notes

Some directories have slower test discovery due to:
1. Large number of test files
2. Complex imports in integration tests
3. Heavy module initialization

**Recommendation:** Test subdirectories individually for faster feedback during development.

## Running Tests

### Quick Test Commands

**Test specific areas:**
```bash
# CLI tests
python -m pytest tests/cli/ -v

# Service tests
python -m pytest tests/services/ -v

# Utility tests
python -m pytest tests/utils/ -v

# Specific unit test category
python -m pytest tests/unit/external/ -v
python -m pytest tests/unit/memory/ -v
python -m pytest tests/unit/reasoning/ -v
```

**Test a single file:**
```bash
python -m pytest tests/unit/external/test_fraud_database.py -v
```

**Run all tests:**
```bash
# Standard run (may be slow for discovery)
python -m pytest tests/ -v

# With short traceback
python -m pytest tests/ -v --tb=short

# Stop on first failure
python -m pytest tests/ -v -x

# Run specific test by name
python -m pytest tests/ -v -k "test_fraud_database"
```

### Test Coverage

**Run tests with coverage:**
```bash
python -m pytest tests/ --cov=src --cov-report=html --cov-report=term
```

**View coverage report:**
```bash
# Open build/coverage/html/index.html in browser
```

## Test Changes Needed

### ✅ No Changes Required

After validation, **no test changes are required**:

1. ✅ All imports are working correctly
2. ✅ Test discovery is functional
3. ✅ No broken test files detected
4. ✅ Module paths are correct

### Import Patterns

Tests use the correct import patterns after reorganization:

**Correct patterns (already in use):**
```python
# Import from src
from src.fraud_detection.core.unified_fraud_detection_system import UnifiedFraudDetectionSystem
from src.fraud_detection.external.fraud_database import FraudDatabaseTool

# Import from bedrock_agentcore_starter_toolkit
from bedrock_agentcore_starter_toolkit.services.runtime import Runtime
```

## Test Fixtures

### Shared Fixtures Location

Test fixtures are located in:
- `tests/conftest.py` - Global fixtures
- `tests/fixtures/` - Fixture data and utilities
- `tests/fixtures/data/` - Test data files
- `tests/fixtures/utils/` - Fixture helper utilities

### Using Fixtures

Fixtures are automatically available to all tests via pytest's fixture discovery:

```python
@pytest.fixture
def system():
    """Create unified system for testing."""
    return UnifiedFraudDetectionSystem()

def test_something(system):
    """Test uses the system fixture."""
    result = system.process_transaction(...)
    assert result is not None
```

## Continuous Integration

### CI/CD Recommendations

For CI/CD pipelines, use these commands:

```bash
# Fast smoke test (critical paths only)
python -m pytest tests/cli/ tests/services/ -v --tb=short

# Full test suite with coverage
python -m pytest tests/ -v --tb=short --cov=src --cov-report=xml

# Parallel execution (if pytest-xdist installed)
python -m pytest tests/ -v -n auto --tb=short
```

### GitHub Actions Example

```yaml
- name: Run tests
  run: |
    python -m pytest tests/ -v --tb=short --cov=src --cov-report=xml
    
- name: Upload coverage
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```

## Troubleshooting

### Test Discovery Issues

**Problem:** Tests not being discovered

**Solutions:**
1. Check test file naming (must start with `test_` or end with `_test.py`)
2. Verify `__init__.py` files exist in test directories
3. Check pytest configuration in `pyproject.toml`
4. Run with verbose collection: `python -m pytest --collect-only -v`

### Import Errors

**Problem:** `ModuleNotFoundError` or `ImportError`

**Solutions:**
1. Verify module paths match new structure
2. Check `sys.path` includes `src/` directory
3. Ensure `__init__.py` files exist in module directories
4. Run dependency scan: `python scripts/reorganization/scan_dependencies.py`

### Slow Test Discovery

**Problem:** Test discovery takes too long

**Solutions:**
1. Test subdirectories individually
2. Use pytest markers to categorize tests
3. Install `pytest-xdist` for parallel execution
4. Use `--collect-only` to test discovery without running tests

## Validation Scripts

### Available Scripts

1. **Quick Validation**
   ```bash
   python scripts/reorganization/quick_test_validation.py
   ```
   - Tests each directory individually
   - Identifies problematic areas
   - Provides summary report

2. **Full Validation** (may timeout on large directories)
   ```bash
   python scripts/reorganization/validate_test_suite.py
   ```
   - Comprehensive test suite validation
   - Compares against baseline (if available)
   - Generates detailed report

## Summary

✅ **Test suite is fully functional after reorganization**

- All test directories work correctly
- No import errors detected
- Test discovery is operational
- No test changes required

**Recommendation:** Proceed with confidence - the test suite is ready for use.

---

**Last Updated:** 2025-01-20
**Status:** Complete
