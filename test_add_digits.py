import pytest
from practice import addDigits   # update import based on your file structure

def test_add_digits_basic():
    assert addDigits(123) == 6   # 1+2+3

def test_add_digits_zero():
    assert addDigits(0) == 0

def test_add_digits_single_digit():
    assert addDigits(7) == 7

def test_add_digits_negative_input():
    with pytest.raises(ValueError):
        addDigits(-10)
