import pygame
import random

class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (0, 255, 0),  # Vert
                          [(8, 4), (4, 0), (0, 4), (8, 16), (16, 4), (12, 0)])
        self.rect = self.image.get_rect()
        self.reset_position()
        
    def reset_position(self):
        """
        Resets the position of the heart to a random position on the screen.
        
        The x-coordinate is randomly chosen between 0 and the width of the screen
        minus the width of the heart. The y-coordinate is randomly chosen between
        0 and the height of the screen minus the height of the heart.
        """
        screen = pygame.display.get_surface()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = random.randint(0, screen.get_height() - self.rect.height)
