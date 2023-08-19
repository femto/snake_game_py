import pytest
from solution import find_max

def test_find_max_positive_numbers():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([10, 20, 5, 8, 30]) == 30

def test_find_max_negative_numbers():
    assert find_max([-1, -2, -3, -4, -5]) == -1
    assert find_max([-10, -20, -5, -8, -30]) == -5

def test_find_max_mixed_numbers():
    assert find_max([-1, 2, -3, 4, -5]) == 4
    assert find_max([10, -20, 5, -8, 30]) == 30

def test_find_max_single_element():
    assert find_max([1]) == 1
    assert find_max([-10]) == -10

def test_find_max_duplicate_maximum():
    assert find_max([1, 2, 3, 3, 2, 1]) == 3
