# Repository Migration Guide

This document provides a comprehensive guide for migrating to the new repository structure and name. The repository has been renamed from "bedrock-agentcore-starter-toolkit" to "StarJam" and reorganized to improve code organization, maintainability, and follow Python best practices.

## Table of Contents

- [Repository Rename](#repository-rename)
- [Overview](#overview)
- [What Changed](#what-changed)
- [File Movement Map](#file-movement-map)
- [Import Updates](#import-updates)
- [Configuration Changes](#configuration-changes)
- [Developer Checklist](#developer-checklist)
- [Troubleshooting](#troubleshooting)

---

## Repository Rename

### Overview

The repository has been renamed from `bedrock-agentcore-starter-toolkit` to `starjam` to better reflect the project's identity and simplify references throughout the codebase.

### What Changed

- **Repository Name:** `bedrock-agentcore-starter-toolkit` → `starjam`
- **Package Name:** `bedrock-agentcore-starter-toolkit` → `starjam`
- **GitHub URLs:** All references updated to new repository name
- **Documentation:** All references updated to use "StarJam" branding

### Migration Steps for Existing Users

#### 1. Update Your Git Remote

If you have an existing clone of the repository, update your remote URL:

```bash
git remote set-url origin https://github.com/your-org/starjam.git
```

Verify the change:
```bash
git remote -v
```

#### 2. Rename Your Local Directory (Optional)

For consistency, you may want to rename your local directory:

```bash
cd ..
mv bedrock-agentcore-starter-toolkit starjam
cd starjam
```

#### 3. Update Package Installation

Uninstall the old package and reinstall with the new name:

```bash
pip uninstall bedrock-agentcore-starter-toolkit
pip install -e .
```

#### 4. Update Your Dependencies

If you have the package listed in `requirements.txt` or `pyproject.toml`:

**requirements.txt:**
```txt
# Old
bedrock-agentcore-starter-toolkit

# New
starjam
```

**pyproject.toml:**
```toml
# Old
dependencies = ["bedrock-agentcore-starter-toolkit"]

# New
dependencies = ["starjam"]
```

#### 5. Update CI/CD and Deployment Scripts

Update any scripts or configurations that reference the old repository name:

```bash
# Old
REPO_NAME="bedrock-agentcore-starter-toolkit"
git clone https://github.com/your-org/bedrock-agentcore-starter-toolkit.git

# New
REPO_NAME="starjam"
git clone https://github.com/your-org/starjam.git
```

#### 6. Update Documentation References

Update any internal documentation, wikis, or notes that reference the old name.

### Breaking Changes

- The package name has changed, requiring updates to import statements in external projects
- GitHub URLs have changed, requiring updates to git remotes and CI/CD configurations
- Any hardcoded references to the old name will need to be updated

### Backward Compatibility

- Git history is fully preserved
- All functionality remains the same
- Only naming and references have changed

---

## Overview

The repository has been reorganized to follow a more standard Python project structure with clear separation of concerns:

- **Source code** → `src/fraud_detection/`
- **Tests** → `tests/`
- **Infrastructure** → `infrastructure/`
- **Examples** → `examples/`
- **Documentation** → `docs/`
- **Scripts** → `scripts/`
- **Archive** → `.archive/`

### Key Benefits

- ✅ Standard Python package structure
- ✅ Clear separation of concerns
- ✅ Improved discoverability
- ✅ Better IDE support
- ✅ Simplified CI/CD configuration
- ✅ Easier onboarding for new developers

---

## What Changed

### Directory Structure

**Before:**
```
bedrock-agentcore-starter-toolkit/
├── fraud_detection_agent.py
├── transaction_processing_pipeline.py
├── agent_coordination/
├── specialized_agents/
├── memory_system/
├── reasoning_engine/
├── aws_infrastructure/
├── aws_bedrock_agent/
├── tests/
├── tests_integ/
├── web_interface/
├── stress_testing/
└── (many root-level files)
```

**After:**
```
starjam/
├── src/
│   └── fraud_detection/
│       ├── core/
│       ├── agents/
│       ├── memory/
│       ├── reasoning/
│       ├── streaming/
│       ├── external/
│       └── web/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── infrastructure/
│   └── aws/
├── examples/
│   ├── basic/
│   ├── agents/
│   ├── reasoning/
│   ├── memory/
│   ├── dashboards/
│   └── stress_testing/
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── guides/
│   ├── operations/
│   └── project/
├── scripts/
│   ├── security/
│   ├── release/
│   ├── development/
│   └── utilities/
└── .archive/
```

---

## File Movement Map

### Core Source Code

| Old Location | New Location |
|-------------|--------------|
| `fraud_detection_agent.py` | `src/fraud_detection/core/fraud_detection_agent.py` |
| `transaction_processing_pipeline.py` | `src/fraud_detection/core/transaction_processing_pipeline.py` |
| `unified_fraud_detection_system.py` | `src/fraud_detection/core/unified_fraud_detection_system.py` |
| `fraud_detection_api.py` | `src/fraud_detection/core/fraud_detection_api.py` |

### Agent Modules

| Old Location | New Location |
|-------------|--------------|
| `agent_coordination/` | `src/fraud_detection/agents/coordination/` |
| `specialized_agents/` | `src/fraud_detection/agents/specialized/` |
| `aws_bedrock_agent/` (agent code) | `src/fraud_detection/agents/bedrock/` |

### Memory and Reasoning

| Old Location | New Location |
|-------------|--------------|
| `memory_system/` | `src/fraud_detection/memory/` |
| `reasoning_engine/` | `src/fraud_detection/reasoning/` |

### Streaming and External

| Old Location | New Location |
|-------------|--------------|
| `streaming/` | `src/fraud_detection/streaming/` |
| `external_tools/` | `src/fraud_detection/external/` |

### Web Interfaces

| Old Location | New Location |
|-------------|--------------|
| `web_interface/` | `src/fraud_detection/web/dashboards/` |
| `stress_testing/dashboards/` | `src/fraud_detection/web/dashboards/` (merged) |
| API files | `src/fraud_detection/web/api/` |

### Tests

| Old Location | New Location |
|-------------|--------------|
| `tests/` (module tests) | `tests/unit/` |
| `tests_integ/` | `tests/integration/` |
| Test utilities | `tests/fixtures/` |

### Infrastructure

| Old Location | New Location |
|-------------|--------------|
| `aws_infrastructure/` | `infrastructure/aws/` |
| `aws_bedrock_agent/` (deployment) | `infrastructure/aws/bedrock/` |
| `infrastructure/cdk_app.py` | `infrastructure/cdk/` |
| Deployment scripts | `infrastructure/aws/deployment/` |

### Examples

| Old Location | New Location |
|-------------|--------------|
| `demo_*.py` (root) | `examples/basic/` or category-specific |
| Agent demos | `examples/agents/` |
| Reasoning demos | `examples/reasoning/` |
| Memory demos | `examples/memory/` |
| Dashboard demos | `examples/dashboards/` |
| Stress testing demos | `examples/stress_testing/` |

### Documentation

| Old Location | New Location |
|-------------|--------------|
| `ARCHITECTURE.md` | `docs/architecture/README.md` |
| `API_DOCUMENTATION.md` | `docs/api/API_REFERENCE.md` |
| `DEPLOYMENT_GUIDE.md` | `docs/guides/deployment-guide.md` |
| `OPERATIONS_RUNBOOK.md` | `docs/operations/` |
| `CONTRIBUTING.md` | `docs/project/CONTRIBUTING.md` |
| Quick start guides | `docs/guides/` |

### Scripts

| Old Location | New Location |
|-------------|--------------|
| `security_check.py` | `scripts/security/` |
| `run_security_audit.py` | `scripts/security/` |
| Release scripts | `scripts/release/` |
| Development scripts | `scripts/development/` |
| Utility scripts | `scripts/utilities/` |

### Archive

| Old Location | New Location |
|-------------|--------------|
| `TASK_*.md` | `.archive/task-summaries/` |
| `*_COMPLETION_SUMMARY.md` | `.archive/task-summaries/` |
| `PROJECT_*.md` | `.archive/project-reports/` |

---

## Import Updates

### Old Import Pattern

```python
# Old imports (no longer work)
from fraud_detection_agent import FraudDetectionAgent
from memory_system.memory_manager import MemoryManager
from specialized_agents.transaction_analyzer import TransactionAnalyzer
```

### New Import Pattern

```python
# New imports
from fraud_detection.core.fraud_detection_agent import FraudDetectionAgent
from fraud_detection.memory.memory_manager import MemoryManager
from fraud_detection.agents.specialized.specialized_agents.transaction_analyzer import TransactionAnalyzer
```

### Common Import Mappings

| Old Import | New Import |
|-----------|-----------|
| `from fraud_detection_agent import *` | `from fraud_detection.core.fraud_detection_agent import *` |
| `from memory_system.memory_manager import *` | `from fraud_detection.memory.memory_manager import *` |
| `from memory_system.context_manager import *` | `from fraud_detection.memory.context_manager import *` |
| `from memory_system.models import *` | `from fraud_detection.memory.models import *` |
| `from reasoning_engine.adaptive_reasoning import *` | `from fraud_detection.reasoning.adaptive_reasoning import *` |
| `from streaming.transaction_stream_processor import *` | `from fraud_detection.streaming.transaction_stream_processor import *` |
| `from external_tools.tool_integrator import *` | `from fraud_detection.external.tool_integrator import *` |
| `from specialized_agents.base_agent import *` | `from fraud_detection.agents.specialized.specialized_agents.base_agent import *` |

### Package-Level Imports

The main package exposes commonly used classes:

```python
# Convenient imports from package root
from fraud_detection.agents import BaseAgent
from fraud_detection.memory import MemoryManager, ContextManager
from fraud_detection.core import FraudDetectionAgent
```

---

## Configuration Changes

### pyproject.toml

The package configuration has been updated:

```toml
[project]
name = "starjam"
version = "0.1.12"

[tool.hatch.build.targets.wheel]
packages = ["src/fraud_detection"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]

[tool.coverage.run]
source = ["src/fraud_detection"]

[tool.ruff]
include = ["src/**/*.py", "tests/**/*.py"]
```

### GitHub Actions Workflow

Environment variables updated in `.github/workflows/ci-cd.yml`:

```yaml
env:
  SRC_PATH: 'src'
  TESTS_PATH: 'tests'
  INFRASTRUCTURE_PATH: 'infrastructure'
  SCRIPTS_PATH: 'scripts'
  EXAMPLES_PATH: 'examples'
```

Test commands now use:
```yaml
pytest ${{ env.TESTS_PATH }}/ -v --cov=${{ env.SRC_PATH }}
```

### Package Installation

Install in editable mode for development:

```bash
pip install -e .
```

This allows you to import from `fraud_detection` package while developing.

---

## Developer Checklist

### For Existing Developers

- [ ] Pull the latest changes from the reorganization branch
- [ ] Reinstall the package: `pip install -e .`
- [ ] Update your imports in any local branches
- [ ] Run tests to verify everything works: `pytest tests/`
- [ ] Update any local scripts that reference old paths
- [ ] Review this migration guide for any custom tooling updates

### For New Developers

- [ ] Clone the repository
- [ ] Install dependencies: `pip install -e .`
- [ ] Run tests: `pytest tests/`
- [ ] Review the documentation in `docs/`
- [ ] Check out examples in `examples/`

### For CI/CD

- [ ] Verify GitHub Actions workflows pass
- [ ] Check deployment scripts work with new paths
- [ ] Validate infrastructure deployment scripts
- [ ] Test example scripts run successfully

---

## Troubleshooting

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'fraud_detection_agent'`

**Solution:** Update your imports to use the new package structure:
```python
# Old
from fraud_detection_agent import FraudDetectionAgent

# New
from fraud_detection.core.fraud_detection_agent import FraudDetectionAgent
```

---

**Problem:** `ModuleNotFoundError: No module named 'fraud_detection'`

**Solution:** Reinstall the package in editable mode:
```bash
pip install -e .
```

---

### Test Discovery Issues

**Problem:** Tests not being discovered by pytest

**Solution:** Ensure you're running pytest from the project root:
```bash
pytest tests/
```

Or specify the test path explicitly in your IDE configuration.

---

### Path Issues in Scripts

**Problem:** Scripts can't find files at old locations

**Solution:** Update file paths in your scripts:
```python
# Old
config_path = "aws_infrastructure/config/settings.json"

# New
config_path = "infrastructure/aws/config/settings.json"
```

---

### IDE Not Recognizing Imports

**Problem:** IDE shows import errors even though code runs

**Solution:**
1. Reinstall the package: `pip install -e .`
2. Restart your IDE
3. Ensure your IDE's Python interpreter is set to the correct virtual environment
4. Mark `src/` as a sources root in your IDE settings

---

### Git History Issues

**Problem:** Can't see file history after reorganization

**Solution:** Use `git log --follow` to track files across renames:
```bash
git log --follow src/fraud_detection/core/fraud_detection_agent.py
```

---

### Deployment Issues

**Problem:** Deployment scripts fail with path errors

**Solution:** Update deployment scripts to use new paths:
```bash
# Old
cd aws_infrastructure/deployment

# New
cd infrastructure/aws/deployment
```

---

## Additional Resources

- **Architecture Documentation:** `docs/architecture/README.md`
- **API Reference:** `docs/api/API_REFERENCE.md`
- **Getting Started Guide:** `docs/guides/getting-started.md`
- **Deployment Guide:** `docs/guides/deployment-guide.md`
- **Examples:** `examples/README.md`

---

## Questions or Issues?

If you encounter any issues not covered in this guide:

1. Check the `docs/` directory for detailed documentation
2. Review the examples in `examples/` for working code
3. Check the `.archive/` directory for historical context
4. Open an issue on GitHub with details about your problem

---

## Summary

The repository reorganization provides a cleaner, more maintainable structure that follows Python best practices. While it requires updating imports and paths, the long-term benefits include:

- Better code organization
- Improved developer experience
- Easier testing and CI/CD
- Clearer project structure
- Better IDE support

Thank you for your patience during this transition!
