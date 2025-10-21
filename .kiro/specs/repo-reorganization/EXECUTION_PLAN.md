# Efficient Execution Plan for Tasks 5-13

## Overview
This plan optimizes the execution of the remaining 9 major tasks (5-13) of the repository reorganization. The strategy focuses on minimizing dependencies, enabling parallel work where possible, and maintaining system stability throughout.

## Execution Strategy

### Key Principles
1. **Batch similar operations** - Group file movements and updates together
2. **Validate incrementally** - Test after each major phase to catch issues early
3. **Preserve functionality** - Ensure the system remains operational throughout
4. **Automate repetitive tasks** - Use scripts for import updates and validation

### Dependency Analysis

```
Task 5 (Infrastructure) ─┐
Task 6 (Examples)       ─┼─→ Task 10 (Config) ─→ Task 11 (Validation) ─→ Task 12 (Docs) ─→ Task 13 (Cleanup)
Task 7 (Documentation)  ─┤
Task 8 (Scripts)        ─┤
Task 9 (Archive)        ─┘
```

**Independent Tasks (Can run in parallel):**
- Task 5: Infrastructure consolidation
- Task 6: Examples and demos
- Task 7: Documentation consolidation
- Task 8: Scripts organization
- Task 9: Archive artifacts

**Dependent Tasks (Must run sequentially):**
- Task 10: Configuration updates (needs all file movements complete)
- Task 11: Comprehensive validation (needs config updates)
- Task 12: Migration documentation (needs validation results)
- Task 13: Final cleanup (needs everything complete)

## Optimized Execution Plan

### Phase 1: Parallel File Movements (Tasks 5-9)
**Duration: ~2-3 hours**
**Goal: Move all remaining files to their target locations**

Execute these tasks in parallel or rapid succession since they don't depend on each other:

#### Task 5: Infrastructure Consolidation
```bash
# 5.1 Merge AWS infrastructure directories
- Move aws_infrastructure/ → infrastructure/aws/
- Move aws_bedrock_agent/ deployment → infrastructure/aws/bedrock/
- Move infrastructure/cdk_app.py → infrastructure/cdk/
- Organize by AWS service

# 5.2 Organize deployment scripts  
- Move scripts/deploy_blue_green.sh → infrastructure/aws/deployment/
- Move scripts/rollback_deployment.sh → infrastructure/aws/deployment/

# 5.3 Update infrastructure configuration
- Move config files → infrastructure/aws/config/
- Update import paths
- Create infrastructure/README.md
```

**Automation Opportunity:**
```python
# Use existing scripts/reorganization/complete_reorganization.py
# Add infrastructure movements to movement_plan.json
```

#### Task 6: Examples and Demos
```bash
# 6.1 Move basic examples
- demo_transaction_stream.py → examples/basic/
- agent_example.py → examples/basic/
- Simple fraud demos → examples/basic/

# 6.2 Move agent examples
- demo_agent_*.py → examples/agents/
- demo_workload_distribution.py → examples/agents/

# 6.3 Move reasoning and memory examples
- demo_reasoning*.py → examples/reasoning/
- demo_memory*.py → examples/memory/
- demo_pattern*.py → examples/memory/

# 6.4 Move dashboard examples
- demo_*_dashboard.py → examples/dashboards/
- demo_analytics*.py → examples/dashboards/
- HTML demo files → examples/dashboards/

# 6.5 Move stress testing examples
- stress_testing/demo_*.py → examples/stress_testing/
- Keep stress_testing core in src/

# 6.6 Create examples/README.md
```

**Batch Operation:**
```bash
# Create a batch movement script for all demo_*.py files
find . -maxdepth 1 -name "demo_*.py" -type f | while read file; do
    # Categorize and move based on filename
done
```

#### Task 7: Documentation Consolidation
```bash
# 7.1 Merge API documentation
- API_DOCUMENTATION.md → docs/api/
- docs/API_REFERENCE.md → docs/api/
- Merge duplicates

# 7.2 Organize architecture docs
- docs/ARCHITECTURE.md → docs/architecture/

# 7.3 Consolidate user guides
- Quick-start guides → docs/guides/
- Merge dashboard guides
- Create unified getting-started.md

# 7.4 Organize operations docs
- docs/OPERATIONS_RUNBOOK.md → docs/operations/
- docs/TROUBLESHOOTING.md → docs/operations/

# 7.5 Move project meta-docs
- CONTRIBUTING.md → docs/project/
- CODE-OF-CONDUCT.md → docs/project/
- CHANGELOG.md → docs/project/

# 7.6 Create docs/README.md navigation

# 7.7 Update documentation links
```

**Link Update Automation:**
```python
# Scan all .md files for internal links
# Update paths based on movement_plan.json
# Verify all links resolve
```

#### Task 8: Scripts Organization
```bash
# 8.1 Organize security scripts
- security_check.py → scripts/security/
- run_security_audit.py → scripts/security/
- quick_security_check.sh → scripts/security/

# 8.2 Organize release scripts
# (Already in scripts/release/)

# 8.3 Organize development scripts
- scripts/setup-branch-protection.sh → scripts/development/
- tests/run_all_tests.py → scripts/development/

# 8.4 Organize utility scripts
- currency_converter.py → scripts/utilities/
- data_loader.py → scripts/utilities/
- transaction_generator.py → scripts/utilities/
- check_models.py → scripts/utilities/
- test_*.py (root) → tests/unit/ or tests/integration/

# 8.5 Create scripts/README.md
```

#### Task 9: Archive Artifacts
```bash
# 9.1 Archive task summaries
- TASK_*.md → .archive/task-summaries/
- *_COMPLETION_SUMMARY.md → .archive/task-summaries/
- *_SUMMARY.md → .archive/task-summaries/

# 9.2 Archive project reports
- PROJECT_*.md → .archive/project-reports/
- FINAL_PROJECT_SUMMARY.md → .archive/project-reports/
- MOBILE_UPDATE_SUMMARY.md → .archive/project-reports/

# 9.3 Create .archive/README.md
```

**Batch Archive Operation:**
```bash
# Single command to move all summary files
find . -maxdepth 2 -name "*SUMMARY*.md" -o -name "TASK_*.md" | \
  xargs -I {} git mv {} .archive/task-summaries/
```

**Phase 1 Validation:**
```bash
# Quick validation after Phase 1
python scripts/reorganization/scan_dependencies.py
python scripts/reorganization/update_imports.py --dry-run
```

---

### Phase 2: Configuration Updates (Task 10)
**Duration: ~1 hour**
**Goal: Update all configuration files to reflect new structure**

#### Task 10: Update Configuration Files
```bash
# 10.1 Update pyproject.toml
[tool.hatch.build.targets.wheel]
packages = ["src/fraud_detection"]

[tool.ruff]
include = ["src/**/*.py", "tests/**/*.py"]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.coverage.run]
source = ["src/fraud_detection"]

# 10.2 Update GitHub Actions workflows
# Update .github/workflows/ci-cd.yml
- Update test paths
- Update deployment script paths
- Use variables for maintainability

# 10.3 Update pre-commit configuration
# Verify .pre-commit-config.yaml works with new structure

# 10.4 Update ruff and mypy configurations
# Verify linting works with new paths
```

**Automation:**
```python
# Create scripts/reorganization/update_configs.py
# Programmatically update all config files
# Validate syntax after updates
```

**Phase 2 Validation:**
```bash
# Validate configurations
python -m pytest --collect-only  # Test discovery
ruff check src/ tests/            # Linting
mypy src/                         # Type checking
```

---

### Phase 3: Comprehensive Validation (Task 11)
**Duration: ~1-2 hours**
**Goal: Ensure everything works correctly**

#### Task 11: Run Comprehensive Validation
```bash
# 11.1 Create and run import validation
python scripts/reorganization/validate_imports.py
# Validates all modules can be imported

# 11.2 Run full test suite
pytest tests/ -v --cov=src/fraud_detection
# Compare against baseline from Task 1

# 11.3 Test package installation
python -m venv test_env
source test_env/bin/activate  # or test_env\Scripts\activate on Windows
pip install -e .
python -c "from fraud_detection.core import FraudDetectionAgent"
deactivate

# 11.4 Validate examples run successfully
cd examples/basic/
python transaction_stream.py
# Test key examples from each category

# 11.5 Test CI/CD pipeline
git push origin feature/reorganization
# Monitor GitHub Actions
```

**Validation Checklist:**
- [ ] All imports resolve
- [ ] All tests pass
- [ ] Package installs correctly
- [ ] Examples run without errors
- [ ] CI/CD pipeline passes
- [ ] No regression in functionality
- [ ] Code coverage maintained

**Phase 3 Output:**
- Validation report documenting all results
- List of any issues found
- Comparison against baseline metrics

---

### Phase 4: Documentation (Task 12)
**Duration: ~2 hours**
**Goal: Document the reorganization for developers**

#### Task 12: Create Migration Documentation
```bash
# 12.1 Create MIGRATION.md
- Complete file movement map
- Import update examples
- Configuration changes
- Developer checklist
- Troubleshooting section

# 12.2 Update README.md
- Add project structure section with directory tree
- Update quick start instructions
- Update import examples
- Add navigation links to docs
- Update badges and links

# 12.3 Create reorganization summary
- Document rationale for decisions
- Summarize changes
- Provide before/after comparison
```

**Documentation Template:**
```markdown
# MIGRATION.md

## File Movement Map
| Old Path | New Path | Type |
|----------|----------|------|
| fraud_detection_agent.py | src/fraud_detection/core/fraud_detection_agent.py | Core |
| demo_transaction_stream.py | examples/basic/transaction_stream.py | Example |
| ... | ... | ... |

## Import Updates
### Before
```python
from fraud_detection_agent import FraudDetectionAgent
```

### After
```python
from fraud_detection.core.fraud_detection_agent import FraudDetectionAgent
```

## Configuration Changes
- pyproject.toml: Updated package paths
- pytest: Updated testpaths
- CI/CD: Updated workflow paths

## Developer Checklist
- [ ] Pull latest changes
- [ ] Update local imports
- [ ] Run tests locally
- [ ] Update custom scripts

## Troubleshooting
...
```

---

### Phase 5: Final Cleanup (Task 13)
**Duration: ~30 minutes**
**Goal: Polish and finalize the reorganization**

#### Task 13: Final Cleanup and Verification
```bash
# 13.1 Clean up empty directories
find . -type d -empty -delete
# Remove __pycache__ directories
find . -type d -name "__pycache__" -exec rm -rf {} +

# 13.2 Verify git history preservation
git log --follow src/fraud_detection/core/fraud_detection_agent.py
git blame src/fraud_detection/core/fraud_detection_agent.py

# 13.3 Run final comprehensive validation
# Repeat all validation steps from Task 11
pytest tests/ -v --cov=src/fraud_detection --cov-report=html
python scripts/reorganization/validate_imports.py
pip install -e . && python -c "import fraud_detection"

# 13.4 Create validation report
# Document all validation results
# List any known issues
# Provide success metrics

# 13.5 Merge to main branch
git checkout main
git merge feature/reorganization
git push origin main
git tag v2.0.0-reorganized
git push origin v2.0.0-reorganized
```

**Final Checklist:**
- [ ] No empty directories
- [ ] Git history preserved
- [ ] All tests pass
- [ ] All imports work
- [ ] Package installs
- [ ] Examples run
- [ ] CI/CD passes
- [ ] Documentation complete
- [ ] Validation report created
- [ ] Changes merged to main

---

## Execution Timeline

### Recommended Schedule

**Day 1: Phase 1 (Tasks 5-9)**
- Morning: Tasks 5-6 (Infrastructure + Examples)
- Afternoon: Tasks 7-9 (Docs + Scripts + Archive)
- End of day: Phase 1 validation

**Day 2: Phases 2-3 (Tasks 10-11)**
- Morning: Task 10 (Configuration updates)
- Afternoon: Task 11 (Comprehensive validation)
- End of day: Review validation results

**Day 3: Phases 4-5 (Tasks 12-13)**
- Morning: Task 12 (Documentation)
- Afternoon: Task 13 (Final cleanup)
- End of day: Merge to main

**Total Estimated Time: 2-3 days**

---

## Automation Scripts to Use

### Existing Scripts (Already Created)
1. `scripts/reorganization/scan_dependencies.py` - Dependency analysis
2. `scripts/reorganization/update_imports.py` - Import statement updates
3. `scripts/reorganization/movement_plan.json` - File movement mapping
4. `scripts/reorganization/complete_reorganization.py` - Orchestration

### New Scripts to Create
1. `scripts/reorganization/batch_move_demos.py` - Batch move demo files
2. `scripts/reorganization/update_configs.py` - Update configuration files
3. `scripts/reorganization/validate_imports.py` - Import validation (Task 11.1)
4. `scripts/reorganization/update_doc_links.py` - Update documentation links
5. `scripts/reorganization/generate_migration_doc.py` - Auto-generate MIGRATION.md

---

## Risk Mitigation

### Checkpoints
After each phase, verify:
1. ✅ No import errors
2. ✅ Tests still pass
3. ✅ Git history preserved
4. ✅ No orphaned files

### Rollback Points
- After Phase 1: Can rollback file movements
- After Phase 2: Can revert config changes
- After Phase 3: Can fix validation issues
- After Phase 4: Can update documentation
- After Phase 5: Can rollback merge

### Backup Strategy
```bash
# Before starting
git checkout -b backup-before-tasks-5-13
git push origin backup-before-tasks-5-13

# Work on feature branch
git checkout -b feature/reorganization-tasks-5-13
```

---

## Success Metrics

### Quantitative Metrics
- [ ] 100% of tests passing (baseline: current pass rate)
- [ ] 0 import errors
- [ ] Code coverage ≥ baseline
- [ ] All CI/CD workflows passing
- [ ] Package installation successful

### Qualitative Metrics
- [ ] Clear, logical directory structure
- [ ] Comprehensive documentation
- [ ] Easy navigation for new developers
- [ ] Professional presentation
- [ ] Maintainable codebase

---

## Quick Reference Commands

### Phase 1: File Movements
```bash
# Update movement plan
vim scripts/reorganization/movement_plan.json

# Execute movements
python scripts/reorganization/complete_reorganization.py --phase infrastructure
python scripts/reorganization/complete_reorganization.py --phase examples
python scripts/reorganization/complete_reorganization.py --phase docs
python scripts/reorganization/complete_reorganization.py --phase scripts
python scripts/reorganization/complete_reorganization.py --phase archive

# Update imports
python scripts/reorganization/update_imports.py --execute
```

### Phase 2: Configuration
```bash
# Update configs
python scripts/reorganization/update_configs.py

# Validate
pytest --collect-only
ruff check src/ tests/
```

### Phase 3: Validation
```bash
# Full validation suite
python scripts/reorganization/validate_imports.py
pytest tests/ -v --cov=src/fraud_detection
pip install -e . && python -c "import fraud_detection"
```

### Phase 4: Documentation
```bash
# Generate migration doc
python scripts/reorganization/generate_migration_doc.py

# Update README
vim README.md
```

### Phase 5: Cleanup
```bash
# Clean up
find . -type d -empty -delete
find . -type d -name "__pycache__" -exec rm -rf {} +

# Final validation
pytest tests/ -v --cov=src/fraud_detection --cov-report=html

# Merge
git checkout main
git merge feature/reorganization-tasks-5-13
git push origin main
```

---

## Next Steps

To execute this plan:

1. **Review this plan** - Ensure you understand each phase
2. **Prepare environment** - Create backup branch, ensure clean working directory
3. **Start Phase 1** - Begin with parallel file movements (Tasks 5-9)
4. **Validate incrementally** - Test after each phase
5. **Document as you go** - Keep notes for MIGRATION.md
6. **Execute systematically** - Follow the phases in order

**Ready to begin? Start with Phase 1, Task 5.1: Merge AWS infrastructure directories**
