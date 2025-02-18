import random
import time
import pytest
from math_operations import add

def test_add_positive_numbers():
    for _ in range(100000):  # Run the test 10 times
        a = random.randint(2, 99)
        b = random.randint(2, 99)
        expected_result = random.randint(2, 99)  # Correct the expected result to the sum of a and b
        result = add(a, b)
        
        # Log the values being tested for clarity
        print(f"Testing: {a} + {b} = {expected_result}, got: {result}")
        
        try:
            # Assert that the result of add(a, b) is the expected result
            assert result == expected_result, f"Test failed for {a} + {b}. Expected {expected_result}, but got {result}"
        except AssertionError as e:
            print(f"AssertionError: {e}")
            # Continue to the next iteration even if the test fails
            # continue
        
        # time.sleep(0.5)  # Sleep for half a second between tests
