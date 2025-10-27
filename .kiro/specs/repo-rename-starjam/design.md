# Design Document

## Overview

This design outlines the approach for renaming the repository from "bedrock-agentcore-starter-toolkit" to "StarJam". The renaming will be performed through systematic text replacements across configuration files, documentation, and code references while maintaining the existing package structure and functionality.

## Architecture

### Renaming Strategy

The renaming follows a layered approach:

1. **Package Name Layer**: Update Python package metadata in pyproject.toml
2. **Repository Reference Layer**: Update all GitHub URLs and repository references
3. **Documentation Layer**: Update all user-facing documentation
4. **Configuration Layer**: Update CI/CD, deployment scripts, and configuration files
5. **Code Reference Layer**: Update logging, comments, and internal references

### Naming Conventions

- **Repository Name**: `starjam` (lowercase, GitHub standard)
- **Package Name**: `starjam` (lowercase, Python package standard)
- **Display Name**: `StarJam` (title case, branding)
- **Project Title**: `StarJam Starter Toolkit` (full branding)

## Components and Interfaces

### 1. Package Configuration Component

**File**: `pyproject.toml`

**Changes**:
- `name`: `bedrock-agentcore-starter-toolkit` → `starjam`
- `project.urls.Homepage`: Update GitHub URL
- `project.urls["Bug Tracker"]`: Update GitHub URL
- `project.urls.Documentation`: Update GitHub URL

**Rationale**: Central package metadata that affects installation and distribution.

### 2. Documentation Component

**Files**:
- `README.md`
- `MIGRATION.md`
- `REORGANIZATION_COMPLETE.md`
- `docs/**/*.md`

**Changes**:
- GitHub URLs: `your-org/bedrock-agentcore-starter-toolkit` → `your-org/starjam`
- Clone commands: Update repository name
- Badge URLs: Update repository references
- Installation paths: Update directory names in examples

**Rationale**: User-facing documentation must reflect the new branding consistently.

### 3. CI/CD Configuration Component

**Files**:
- `.github/workflows/*.yml`
- `buildspec-lambda-package.yml`

**Changes**:
- Workflow names and references
- Repository references in comments
- Build artifact names (if applicable)

**Rationale**: Ensure CI/CD pipelines reference the correct repository.

### 4. Deployment Scripts Component

**Files**:
- `infrastructure/aws/deployment/*.sh`
- `scripts/development/*.sh`
- `scripts/release/*.py`

**Changes**:
- Repository name references in scripts
- Logging messages and output
- Configuration file references

**Rationale**: Deployment automation must use correct naming.

### 5. Code References Component

**Files**:
- `src/bedrock_agentcore_starter_toolkit/utils/logging_config.py`
- `src/bedrock_agentcore_starter_toolkit/services/import_agent/assets/*.j2`

**Changes**:
- Docstrings and comments
- Logging configuration names
- Template file references

**Rationale**: Internal code references should be consistent with the new name.

### 6. Lock Files and Generated Content

**Files**:
- `uv.lock`

**Changes**:
- Package name references (will be regenerated)

**Rationale**: Lock files will be updated automatically on next dependency resolution.

## Data Models

### File Change Tracking

```python
FileChange = {
    "path": str,              # Relative file path
    "old_value": str,         # Text to replace
    "new_value": str,         # Replacement text
    "line_numbers": List[int] # Lines affected (for verification)
}
```

### Replacement Patterns

```python
ReplacementPattern = {
    "pattern": str,                    # Search pattern (can be regex)
    "replacement": str,                # Replacement string
    "file_patterns": List[str],        # Glob patterns for files to update
    "exclude_patterns": List[str],     # Glob patterns to exclude
    "case_sensitive": bool             # Whether match is case-sensitive
}
```

## Replacement Patterns

### Pattern 1: GitHub Repository URLs

- **Pattern**: `github\.com/your-org/bedrock-agentcore-starter-toolkit`
- **Replacement**: `github.com/your-org/starjam`
- **Files**: `*.md`, `*.yml`, `*.yaml`, `*.py`, `*.sh`
- **Case Sensitive**: Yes

### Pattern 2: Package Name in pyproject.toml

- **Pattern**: `name = "bedrock-agentcore-starter-toolkit"`
- **Replacement**: `name = "starjam"`
- **Files**: `pyproject.toml`
- **Case Sensitive**: Yes

### Pattern 3: Clone Commands

- **Pattern**: `git clone https://github.com/your-org/bedrock-agentcore-starter-toolkit.git`
- **Replacement**: `git clone https://github.com/your-org/starjam.git`
- **Files**: `*.md`
- **Case Sensitive**: Yes

### Pattern 4: Directory References

- **Pattern**: `cd bedrock-agentcore-starter-toolkit`
- **Replacement**: `cd starjam`
- **Files**: `*.md`, `*.sh`
- **Case Sensitive**: Yes

### Pattern 5: Logging Configuration

- **Pattern**: `bedrock-agentcore-starter-toolkit` (in docstrings and function names)
- **Replacement**: `starjam`
- **Files**: `src/**/*.py`
- **Case Sensitive**: Yes

### Pattern 6: Template Requirements

- **Pattern**: `bedrock-agentcore-starter-toolkit` (in .j2 templates)
- **Replacement**: `starjam`
- **Files**: `**/*.j2`
- **Case Sensitive**: Yes

### Pattern 7: Script Repository References

- **Pattern**: `REPO_NAME="bedrock-agentcore-starter-toolkit-staging"`
- **Replacement**: `REPO_NAME="starjam-staging"`
- **Files**: `scripts/**/*.sh`, `scripts/**/*.py`
- **Case Sensitive**: Yes

### Pattern 8: Project Structure Diagrams

- **Pattern**: `bedrock-agentcore-starter-toolkit/` (in directory trees)
- **Replacement**: `starjam/`
- **Files**: `*.md`
- **Case Sensitive**: Yes

## Error Handling

### File Not Found

- **Strategy**: Log warning and continue with other files
- **Recovery**: Manual verification of expected files

### Permission Errors

- **Strategy**: Report error and skip file
- **Recovery**: User must fix permissions and retry

### Encoding Issues

- **Strategy**: Try UTF-8, fallback to system encoding
- **Recovery**: Report files with encoding issues for manual review

### Backup Strategy

- **Approach**: Git-based (rely on version control)
- **Rationale**: All changes are tracked in git, easy to revert
- **Verification**: Use `git diff` to review all changes before commit

## Testing Strategy

### Pre-Change Validation

1. Verify git working directory is clean
2. Identify all files containing the old name
3. Generate change report for review

### Post-Change Validation

1. **Syntax Validation**: Ensure all modified files have valid syntax
   - Python files: Run `python -m py_compile`
   - YAML files: Run `yaml.safe_load()`
   - Markdown files: Check for broken links

2. **Package Installation**: Verify package can be installed
   - Run `pip install -e .`
   - Import main modules to verify no import errors

3. **Configuration Validation**: Check configuration files
   - Parse pyproject.toml
   - Validate CI/CD workflow syntax

4. **Documentation Links**: Verify no broken internal links
   - Check relative links in markdown files
   - Verify badge URLs are accessible

### Rollback Plan

If issues are detected:
1. Use `git reset --hard HEAD` to revert all changes
2. Review the change report
3. Fix any issues in the replacement patterns
4. Re-run the renaming process

## Migration Guide Updates

### MIGRATION.md Additions

Add a new section documenting the repository rename:

```markdown
## Repository Rename (v0.2.0)

The repository has been renamed from `bedrock-agentcore-starter-toolkit` to `starjam`.

### For Existing Users

1. Update your git remote:
   ```bash
   git remote set-url origin https://github.com/your-org/starjam.git
   ```

2. Update your local clone directory (optional):
   ```bash
   cd ..
   mv bedrock-agentcore-starter-toolkit starjam
   cd starjam
   ```

3. Reinstall the package:
   ```bash
   pip uninstall bedrock-agentcore-starter-toolkit
   pip install -e .
   ```

### Package Name Change

The Python package name has changed from `bedrock-agentcore-starter-toolkit` to `starjam`.
Update your requirements.txt or pyproject.toml accordingly.
```

## Implementation Approach

### Phase 1: Preparation
- Verify git status is clean
- Create a feature branch for the rename
- Generate comprehensive file list with occurrences

### Phase 2: Core Configuration
- Update pyproject.toml
- Update package metadata
- Verify package structure remains intact

### Phase 3: Documentation
- Update README.md
- Update all markdown documentation
- Update migration guide

### Phase 4: Infrastructure
- Update CI/CD workflows
- Update deployment scripts
- Update development scripts

### Phase 5: Code References
- Update Python source files
- Update template files
- Update configuration files

### Phase 6: Validation
- Run syntax checks
- Test package installation
- Verify imports work
- Check documentation links

### Phase 7: Cleanup
- Regenerate lock files if needed
- Update any generated documentation
- Final review of all changes

## Success Criteria

1. All references to "bedrock-agentcore-starter-toolkit" are replaced with "starjam" (except in historical documentation)
2. Package can be installed successfully with `pip install -e .`
3. All Python modules can be imported without errors
4. CI/CD workflows pass syntax validation
5. Documentation links are not broken
6. Git history is preserved
7. Migration guide is updated with clear instructions
