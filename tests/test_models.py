"""
Test models module.
"""

from src.models import create_model


def test_create_model():
    assert create_model() is not None
    assert hasattr(create_model(), "fit")
    assert hasattr(create_model(), "predict")