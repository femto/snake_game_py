import pytest
from solution import will_collide

def test_will_collide():
    # Test for collision
    assert will_collide([(5, 5), (5, 6), (5, 7)], ["UP", "UP", "RIGHT"]) == True
    
    # Test for no collision
    assert will_collide([(5, 5), (5, 6), (5, 7)], ["DOWN", "RIGHT", "UP"]) == False
