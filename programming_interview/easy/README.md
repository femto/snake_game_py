# Easy Challenge: Snake's Next Position

## Introduction
In the classic snake game, the snake moves in a certain direction until that direction is changed by the player. Your task is to determine the next position of the snake's head given its current position and direction.

## Problem Statement
Write a function `next_position` that takes in two arguments:

1. A tuple representing the current position of the snake's head as `(x, y)`.
2. A string representing the current direction of the snake, which can be one of the following: "UP", "DOWN", "LEFT", "RIGHT".

The function should return a tuple representing the next position of the snake's head after moving one step in the given direction.

## Input-Output Specifications
- Input:
  - A tuple `(x, y)` where `0 <= x, y < 100`.
  - A string `direction` which is one of "UP", "DOWN", "LEFT", "RIGHT".
- Output:
  - A tuple `(new_x, new_y)` representing the next position.

## Example Cases
1. Input: `(5, 5), "UP"`
   Output: `(5, 4)`
2. Input: `(5, 5), "DOWN"`
   Output: `(5, 6)`
3. Input: `(5, 5), "LEFT"`
   Output: `(4, 5)`
4. Input: `(5, 5), "RIGHT"`
   Output: `(6, 5)`

**Note**: Write your solution in the `solution.py` file in this directory.
