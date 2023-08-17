"""main.py: Main entry point for the Snake game using pygame."""
import sys
sys.path.append("..")
import pygame
from snake_game_py.snake import Snake
from snake_game_py.food import Food
from snake_game_py.ui import UI
from snake_game_py.sounds import Sounds
from snake_game_py.config import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")

        self.score = 0
        self.is_paused = False
        self.snake = Snake()
        self.food = Food()
        self.ui = UI(self.screen)
        self.sounds = Sounds()

    def start(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    self.handle_key_event(event)

            if not self.is_paused:
                self.update()
                self.render()

            clock.tick(10)

    def handle_key_event(self, event):
        if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
            if not self.snake.is_opposite_direction(event.key):
                self.snake.direction = event.key
        if event.key == pygame.K_SPACE:
            self.pause_or_resume()

    def pause_or_resume(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.ui.display_pause_message()

    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.sounds.play_collision_sound()
            self.reset_game()
        elif self.snake.segments[0] == self.food.position:
            self.sounds.play_eat_sound()
            self.score += 1
            self.snake.grow()
            self.food.generate()
            self.ui.display_score(self.score)

    def render(self):
        self.screen.fill((255, 255, 255))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.ui.display_score(self.score)
        pygame.display.flip()

    def reset_game(self):
        self.score = 0
        self.snake = Snake()
        self.food.generate()

#aaabbbcccddd
if __name__ == "__main__":
    game = Game()
    game.start()
