import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (128, 0, 0),  # Rouge foncé
                          [(15, 0), (30, 30), (0, 30)])
        self.rect = self.image.get_rect()
        self.reset_position()
        self.speed = random.randint(2, 5)

    def reset_position(self):
        screen = pygame.display.get_surface()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += self.speed
        screen = pygame.display.get_surface()
        if self.rect.top > screen.get_height():
            self.reset_position()
