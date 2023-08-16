## config.py

# Screen dimensions
SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 480

# Block size for both snake and food
BLOCK_SIZE: int = 20

# Colors (R, G, B)
WHITE: tuple[int, int, int] = (255, 255, 255)
GREEN: tuple[int, int, int] = (0, 255, 0)
RED: tuple[int, int, int] = (255, 0, 0)
BLACK: tuple[int, int, int] = (0, 0, 0)

# Sound files paths
EAT_SOUND_PATH: str = "sounds/eat.wav"
COLLISION_SOUND_PATH: str = "sounds/collision.wav"
