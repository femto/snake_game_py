## snake.py

"""snake.py: Contains the Snake class responsible for snake logic."""

import pygame
from typing import List
from snake_game_py.config import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


class Direction:
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT


class Snake:
    def __init__(self):
        self.segments: List[Point] = [Point(5, 5)]
        self.direction = Direction.RIGHT

    def move(self):
        head = self.segments[0]
        new_head = Point(head.x, head.y)

        if self.direction == Direction.RIGHT:
            new_head.x += 1
        elif self.direction == Direction.LEFT:
            new_head.x -= 1
        elif self.direction == Direction.UP:
            new_head.y -= 1
        elif self.direction == Direction.DOWN:
            new_head.y += 1

        self.segments.insert(0, new_head)
        self.segments.pop()

    def grow(self):
        tail = self.segments[-1]
        self.segments.append(tail)

    def check_collision(self) -> bool:
        head = self.segments[0]
        # Check self collision
        if head in self.segments[1:]:
            return True

        # Check boundary collision
        if (head.x < 0 or head.x >= (SCREEN_WIDTH // BLOCK_SIZE) or
            head.y < 0 or head.y >= (SCREEN_HEIGHT // BLOCK_SIZE)):
            return True

        return False

    def is_opposite_direction(self, new_direction) -> bool:
        opposites = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        return opposites.get(self.direction) == new_direction

    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, (0, 255, 0), 
                             (segment.x * BLOCK_SIZE, segment.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    
    class EnemySnake(Snake):
    def move(self):
        import random
        directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        self.direction = random.choice(directions)
        
        super().move()
    
    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, (255, 0, 0), 
                             (segment.x * BLOCK_SIZE, segment.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))