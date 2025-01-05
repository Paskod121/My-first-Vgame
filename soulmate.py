import pygame

class Soulmate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (255, 215, 0),  # Or
                          [(16, 8), (8, 0), (0, 8), (16, 32), (32, 8), (24, 0)])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
