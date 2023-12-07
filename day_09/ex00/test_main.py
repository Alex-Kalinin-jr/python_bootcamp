import sys
import os
import pytest

EPS_C = 0.000001

sys.path.append(os.path.abspath('./build/lib.*'))
import math_methods

def test_add():
    for a in range (-1000, 1000):
        for b in range (-1000, 1000):
            assert math_methods.add(a, b) == a + b

def test_sub():
    for a in range (-1000, 1000):
        for b in range (-1000, 1000):
            assert math_methods.sub(a, b) == a - b

def test_mul():
    for a in range (-1000, 1000):
        for b in range (-1000, 1000):
            assert math_methods.mul(a, b) == a * b

def test_add_fract():
    xs = (x * 0.1 for x in range(0, 10))
    yx = (y * 0.1 for y in range(0, 10))
    for x in xs:
        for y in yx:
            assert math_methods.add(x, y) == x + y

def test_sub_fract():
    xs = (x * 0.1 for x in range(0, 10))
    yx = (y * 0.1 for y in range(0, 10))
    for x in xs:
        for y in yx:
            assert math_methods.sub(x, y) == x - y

def test_mul_fract():
    xs = (x * 0.1 for x in range(0, 10))
    yx = (y * 0.1 for y in range(0, 10))
    for x in xs:
        for y in yx:
            assert math_methods.mul(x, y) == x * y

def test_div_fract():
    xs = (x * 0.1 for x in range(0, 10))
    yx = (y * 0.1 for y in range(0, 10))
    for x in xs:
        for y in yx:
            if (y == 0):
                with pytest.raises(ZeroDivisionError):
                    math_methods.div(x, y)
            else:
                assert math_methods.mul(x, y) == x * y



