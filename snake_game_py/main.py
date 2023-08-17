"""main.py: Main entry point for the Snake game using pygame."""
import sys
sys.path.append("..")
import pygame
from snake_game_py.game import Game
from snake_game_py.snake import Snake
from snake_game_py.food import Food
from snake_game_py.ui import UI
from snake_game_py.sounds import Sounds
from snake_game_py.config import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
