"""main.py: Main entry point for the Snake game using pygame."""
import sys
from snake_game_py.game import Game
if __name__ == "__main__":
    game = Game()
    game.start()