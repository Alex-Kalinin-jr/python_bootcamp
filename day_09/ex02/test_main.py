import pytest
import random
from time import monotonic
import mul_standard as ms
import mul_cython as mc
import mul_cython_standard as mcs


def test_exceptions_length():
    x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    y = [[1,2],[1,2]]
    with pytest.raises(TypeError):
        ms.mul(x, y)
    with pytest.raises(TypeError):
        mc.mul(x, y)

def test_exceptions_type():
    x = [[1.2,2,3],[4,5,6],[7,8,9],[10,11,12]]
    y = [[1,2],[1,2]]
    with pytest.raises(TypeError):
        ms.mul(x, y)
    with pytest.raises(TypeError):
        mc.mul(x, y)

def test_exceptions_length_2():
    x = [[1,2,3],[4,5,6],[7,8,9],[10,11]]
    y = [[1,2],[1,2],[3,4]]
    with pytest.raises(TypeError):
        ms.mul(x, y)
    with pytest.raises(TypeError):
        mc.mul(x, y)

def test_one():
    x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    y = [[1,2],[1,2],[3,4]]
    assert ms.mul(x, y) == mc.mul(x, y)

def test_two():
    x = [[1,2,3,0],[4,5,6,0],[7,8,9,0],[10,11,12,0]]
    y = [[1,2],[1,2],[3,4],[-1000,1000]]
    assert ms.mul(x, y) == mc.mul(x, y)


def test_three():
    x = [[1,2,3,0],[4,5,6,0],[7,8,9,0],[10,11,12,0]]
    y = [[1,2,3,0],[4,5,6,0],[7,8,9,0],[10,11,12,0]]
    assert ms.mul(x, y) == mc.mul(x, y)



def generate_random_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def test_time():
    x = generate_random_matrix(99, 99)
    y = generate_random_matrix(99, 99)

    start = monotonic()
    ms.mul(x, y)
    end = monotonic()
    print(f"python: {end - start}")

    start = monotonic()
    mc.mul(x, y)
    end = monotonic()
    print(f"cython: {end - start}")

    start = monotonic()
    mcs.mul(x, y)
    end = monotonic()
    print(f"cython_standard: {end - start}")