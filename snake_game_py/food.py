## food.py
import pygame
import random
from snake_game_py.config import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from snake_game_py.snake import Point  # Import Point from snake.py to avoid redundancy

class Food:
    def __init__(self, snake_segments):
        self.position = Point(0, 0)
        self.snake_segments = snake_segments
        self.generate()

    def generate(self):
        """Generate food at a random position on the screen, ensuring it's not on the snake."""
        while True:
            x = random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE) - 1)
            y = random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE) - 1)
            potential_position = Point(x, y)
            if potential_position not in self.snake_segments:
                self.position = potential_position
                break


    def draw(self, screen):
        """Draw the food on the screen."""
        pygame.draw.rect(screen, (255, 0, 0),
                         #this is it
                         (self.position.x * BLOCK_SIZE, self.position.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

