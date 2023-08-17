## sounds.py
import pygame
from typing import Optional

class Sounds:
    def __init__(self, 
                 eat_sound_file: Optional[str] = "sounds/eating.mp3",
                 collision_sound_file: Optional[str] = "sounds/collision.mp3"):
        """
        Initialize the Sounds class with the paths to the sound files.
        
        :param eat_sound_file: Path to the sound file for eating action.
        :param collision_sound_file: Path to the sound file for collision action.
        """
        self.eat_sound = self._load_sound(eat_sound_file)
        self.collision_sound = self._load_sound(collision_sound_file)

    def _load_sound(self, sound_file: str) -> Optional[pygame.mixer.Sound]:
        """
        Safely load a sound file. If the file is missing, return None.
        
        :param sound_file: Path to the sound file.
        :return: pygame Sound object or None.
        """
        try:
            return pygame.mixer.Sound(sound_file)
        except pygame.error:
            print(f"Warning: Unable to load sound file: {sound_file}")
            return None

    def play_eat_sound(self):
        """
        Play the sound effect for when the snake eats a food item.
        """
        if self.eat_sound:
            self.eat_sound.play()

    def play_collision_sound(self):
        """
        Play the sound effect for when the snake collides with the wall or itself.
        """
        if self.collision_sound:
            self.collision_sound.play()

# Example usage
if __name__ == "__main__":
    pygame.init()
    sounds = Sounds()
    sounds.play_eat_sound()
    sounds.play_collision_sound()
