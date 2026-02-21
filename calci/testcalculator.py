import pytest
from calculator import add, subtract, multiply, divide

# ===== ADD TESTS =====
def test_add_positive():
    assert add(2, 4) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_mixed():
    assert add(-2, 3) == 1

# ===== SUBTRACT TESTS =====
def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_negative():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_result_negative():
    assert subtract(3, 10) == -7

# ===== MULTIPLY TESTS =====
def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_negative():
    assert multiply(-3, 4) == -12

def test_multiply_zero():
    assert multiply(5, 0) == 0

def test_multiply_both_negative():
    assert multiply(-3, -4) == 12

# ===== DIVIDE TESTS =====
def test_divide_positive():
    assert divide(10, 2) == 5.0

def test_divide_negative():
    assert divide(-10, 2) == -5.0

def test_divide_float_result():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)