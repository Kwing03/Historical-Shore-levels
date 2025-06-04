import pytest
from project import calculate_uncertainty_value, calculate_shorelevel_mareograph, calculate_shorelevel_satellite

def test_uncertainty_value():
    assert calculate_uncertainty_value(800)==0.33


def test_shorelevel_mareograph():
    assert calculate_shorelevel_mareograph(4.8, 1.2, 550, 0.508, 0.2)==9.276


def test_shorelevel_satellite():
    assert calculate_shorelevel_satellite(6.1, 1.2, 550, 0.508, 0.2)==9.421
