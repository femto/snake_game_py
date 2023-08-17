"""main.py: Main entry point for the Snake game using pygame."""
import sys
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Calculate the parent directory
parent_dir = os.path.dirname(current_dir)

# Append the parent directory to sys.path
sys.path.append(parent_dir)
from snake_game_py.game import Game

pygame.init()

if __name__ == "__main__":
    game = Game()
    game.start()