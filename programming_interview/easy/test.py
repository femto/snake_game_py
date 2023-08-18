import pytest
from solution import next_position

def test_next_position():
    # Test for moving UP
    assert next_position((5, 5), "UP") == (5, 4)
    
    # Test for moving DOWN
    assert next_position((5, 5), "DOWN") == (5, 6)
    
    # Test for moving LEFT
    assert next_position((5, 5), "LEFT") == (4, 5)
    
    # Test for moving RIGHT
    assert next_position((5, 5), "RIGHT") == (6, 5)
