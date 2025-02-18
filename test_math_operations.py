import pytest
import random
from math_operations import add
import time

def test_add_positive_numbers():
    for _ in range(1000):  # Run the test 10 times to avoid an infinite loop
        a = random.randint(2, 99)
        b = random.randint(2, 99)
        expected_result = a + b
        result = add(a, b)
        assert result == expected_result, f"Test failed for {a} + {b}. Expected {expected_result}, but got {result}"
        time.sleep(0.5)  # Sleep for half a second between tests

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    assert add(-2, 5) == 3

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5
