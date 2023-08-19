"""main.py: Main entry point for the Snake game using pygame."""
import sys

import os
import sys

import pygame

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the current directory
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path if it's not already there
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from snake_game_py.game import Game
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.start()