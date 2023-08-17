"""main.py: Main entry point for the Snake game using pygame."""
import sys
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Calculate the parent directory
parent_dir = os.path.dirname(current_dir)

# Append the parent directory to sys.path
sys.path.append(parent_dir)
import pygame
from snake_game_py.game import Game
from snake_game_py.snake import Snake
from snake_game_py.food import Food
from snake_game_py.ui import UI
from snake_game_py.sounds import Sounds
from snake_game_py.config import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
