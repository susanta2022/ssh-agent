import pytest
import random
from math_operations import add
import time

def test_add_positive_numbers():
    while True:
        time.sleep(.5)
        assert add(random.randint(2,99), random.randint(2,99)) == random.randint(2,99)

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    assert add(-2, 5) == 3

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5
