## ui.py

import pygame
from snake_game_py.config import SCREEN_WIDTH, SCREEN_HEIGHT

class UI:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)

    def display_score(self, score: int):
        """Display the current score on the screen."""
        score_text = f"Score: {score}"
        text_surface = self.font.render(score_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(topleft=(10, 10))
        self.screen.blit(text_surface, text_rect)

    def display_pause_message(self):
        """Display a pause message in the center of the screen."""
        pause_text = "Game Paused. Press SPACE to resume."
        text_surface = self.font.render(pause_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text_surface, text_rect)
