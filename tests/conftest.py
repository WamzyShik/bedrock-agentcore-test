"""Pytest configuration and shared fixtures."""

import pytest
from pathlib import Path

# Add project root to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Fixture paths
FIXTURES_ROOT = Path(__file__).parent / "fixtures"
FIXTURES_DATA_DIR = FIXTURES_ROOT / "data"
FIXTURES_UTILS_DIR = FIXTURES_ROOT / "utils"
