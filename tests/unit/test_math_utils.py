import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from utils.math_utils import add, is_even

def test_add():
    assert add(3,5) == 8
    assert add(-5,7) == 2

def test_even():
    assert is_even(3) == False
    assert is_even(6) == True