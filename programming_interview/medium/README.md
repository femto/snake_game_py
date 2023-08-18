# Medium Challenge: Snake Self-Collision Prediction

## Introduction
In the classic snake game, the snake moves in a certain direction and can collide with itself if it moves into a segment of its body. Your task is to predict if the snake will collide with itself given its current segments and a list of future moves.

## Problem Statement
Write a function `will_collide` that takes in two arguments:

1. A list of tuples representing the current segments of the snake, where each tuple is `(x, y)`.
2. A list of strings representing the future directions the snake will move in, which can be one of the following: "UP", "DOWN", "LEFT", "RIGHT".

The function should return a boolean value: `True` if the snake will collide with itself in the given moves, and `False` otherwise.

## Input-Output Specifications
- Input:
  - A list of tuples `segments` where each tuple is `(x, y)` representing the snake's segments.
  - A list of strings `directions` where each string is one of "UP", "DOWN", "LEFT", "RIGHT" representing the future moves of the snake.
- Output:
  - A boolean value indicating if the snake will collide with itself.

## Example Cases
1. Input: `segments = [(5, 5), (5, 6), (5, 7)], directions = ["UP", "UP", "RIGHT"]`
   Output: `True`
   
2. Input: `segments = [(5, 5), (5, 6), (5, 7)], directions = ["DOWN", "RIGHT", "UP"]`
   Output: `False`

**Note**: Write your solution in the `solution.py` file in this directory.
