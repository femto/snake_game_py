"""main.py: Main entry point for the Snake game using pygame."""
import pygame
import sys
from snake_game_py.game import Game
if __name__ == "__main__":
    pygame.init()
    pygame.font.init() # Initialize the font module
    game = Game()
    game.start()