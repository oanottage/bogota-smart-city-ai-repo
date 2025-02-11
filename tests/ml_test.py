"""
ml_test.py

A simple pytest script with basic tests for the ML training script.

Assumptions:
- The ML training script code is saved in a file named 'ml_script.py'.
- 'ml_script.py' reads the environment variable BASE_PATH and raises
  a ValueError if it is not set or if it does not point to an existing directory.
- These tests illustrate very basic examples for getting started with pytest.
"""

import os
os.chdir("/Users/onassisnottage/Desktop/SMART_CITY_AI/Bogota_Colombia/bogota-smart-city-ai-repo/")
import pytest
import importlib

# Test that the module raises ValueError when BASE_PATH is invalid or not set.
def test_invalid_base_path(monkeypatch, tmp_path):
    # Remove BASE_PATH (if set) and then set it to a non-existent directory.
    monkeypatch.delenv("BASE_PATH", raising=False)
    invalid_path = tmp_path / "nonexistent"
    monkeypatch.setenv("BASE_PATH", str(invalid_path))
    
    # When ml_script.py is imported (or reloaded), it should raise a ValueError.
    with pytest.raises(ValueError, match="Invalid BASE_PATH"):
        from src.models import train_model  # Import the module
        importlib.reload(train_model)  # Force it to re-read BASE_PATH

# Test that the module loads successfully when BASE_PATH is valid.
def test_valid_base_path(monkeypatch, tmp_path):
    # Create a temporary directory to act as a valid BASE_PATH.
    valid_base = tmp_path / "valid_base"
    valid_base.mkdir()
    monkeypatch.setenv("BASE_PATH", str(valid_base))
    
    # Import the module; it should load without error.
    from src.models import train_model
    importlib.reload(train_model)
    
    # Verify that the module's BASE_PATH is set as expected.
    assert train_model.BASE_PATH == str(valid_base)

# Test that the main function exists and is callable.
def test_main_callable(monkeypatch, tmp_path):
    # Set a valid BASE_PATH so that the module initializes correctly.
    valid_base = tmp_path / "valid_base"
    valid_base.mkdir()
    monkeypatch.setenv("BASE_PATH", str(valid_base))
    
    from src.models import train_model
    importlib.reload(train_model)
    
    # Check that the main function is callable (a basic sanity check).
    assert callable(train_model.main)
