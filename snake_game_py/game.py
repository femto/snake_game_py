"""
game.py: Contains the core game loop and main game logic.
"""

import pygame
from snake_game_py.snake import Snake
from snake_game_py.food import Food
from snake_game_py.ui import UI
from snake_game_py.sounds import Sounds
from snake_game_py.config import SCREEN_WIDTH, SCREEN_HEIGHT

# Initializing pygame's functionalities
pygame.init()

class Game:
    def __init__(self):
        # Setting up the display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")

        # Initialize game state
        self.initialize_game_state()
        
        # Game components
        self.ui = UI(self.screen)
        self.sounds = Sounds()

    def initialize_game_state(self):
        self.score = 0
        self.is_paused = False
        self.snake = Snake()
        self.food = Food()

    def start(self):
        # Main game loop
        clock = pygame.time.Clock()
        while True:
            # Handle user events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    self.handle_key_event(event)

            # Game update & render logic
            if not self.is_paused:
                self.update()
                self.render()

            # Keeping the game at a stable speed
            clock.tick(10)

    def handle_key_event(self, event):
        # Respond to arrow key events
        if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
            if not self.snake.is_opposite_direction(event.key):
                self.snake.direction = event.key
        # Pause or resume on space key press
        if event.key == pygame.K_SPACE:
            self.pause_or_resume()

    def pause_or_resume(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.ui.display_pause_message()

    def update(self):
        # Move the snake & check for collisions
        self.snake.move()
        if self.snake.check_collision():
            self.sounds.play_collision_sound()
            self.reset_game()
        # Check if the snake ate the food
        elif self.snake.segments[0] == self.food.position:
            self.sounds.play_eat_sound()
            self.score += 1
            self.snake.grow()
            self.food.generate()
            self.ui.display_score(self.score)

    def render(self):
        # Draw everything on the screen
        self.screen.fill((255, 255, 255))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.ui.display_score(self.score)
        pygame.display.flip()

    def reset_game(self):
        # Reset the game state
        self.initialize_game_state()
        self.food.generate()

if __name__ == "__main__":
    game = Game()
    game.start()
