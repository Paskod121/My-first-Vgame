import pygame
import random

class PowerUp(pygame.sprite.Sprite):
    TYPES = ['speed', 'shield', 'magnet']
    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        self.type = random.choice(self.TYPES)
        
        # Différentes couleurs selon le type
        color = {
            'speed': (0, 255, 0),    # Vert
            'shield': (0, 0, 255),   # Bleu
            'magnet': (255, 255, 0)  # Jaune
        }[self.type]
        
        pygame.draw.circle(self.image, color, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.reset_position()
        
    def reset_position(self):
        screen = pygame.display.get_surface()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = random.randint(0, screen.get_height() - self.rect.height)
