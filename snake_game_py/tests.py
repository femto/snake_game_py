## tests.py: Contains unit tests for the Snake game components.
import pytest
from snake_game_py.snake import Snake, Direction, Point
from snake_game_py.food import Food

def test_snake_initialization():
    snake = Snake()
    assert len(snake.segments) == 1
    assert snake.direction == Direction.RIGHT

def test_snake_move():
    snake = Snake()
    initial_position = snake.segments[0]
    snake.move()
    assert snake.segments[0] == Point(initial_position.x + 1, initial_position.y)

def test_snake_grow():
    snake = Snake()
    initial_length = len(snake.segments)
    snake.grow()
    assert len(snake.segments) == initial_length + 1

def test_snake_collision_with_self():
    snake = Snake()
    snake.segments = [Point(5, 5), Point(6, 5), Point(7, 5)]
    snake.direction = Direction.LEFT
    snake.move()
    assert snake.check_collision()

def test_snake_collision_with_boundary():
    snake = Snake()
    snake.segments = [Point(0, 0)]
    snake.direction = Direction.UP
    snake.move()
    assert snake.check_collision()

def test_food_generate_not_on_snake():
    snake_segments = [Point(5, 5), Point(6, 5), Point(7, 5)]
    food = Food(snake_segments)
    assert food.position not in snake_segments

@pytest.mark.parametrize(
    "current_direction, new_direction, expected_result",
    [
        (Direction.UP, Direction.DOWN, True),
        (Direction.LEFT, Direction.RIGHT, True),
        (Direction.DOWN, Direction.UP, True),
        (Direction.RIGHT, Direction.LEFT, True),
        (Direction.UP, Direction.LEFT, False),
        (Direction.LEFT, Direction.UP, False),
    ],
)
def test_is_opposite_direction(current_direction, new_direction, expected_result):
    snake = Snake()
    snake.direction = current_direction
    assert snake.is_opposite_direction(new_direction) == expected_result
