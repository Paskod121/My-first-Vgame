import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        self.base_image = self.image.copy()
        pygame.draw.polygon(self.base_image, (255, 192, 203),  # Rose
                          [(16, 8), (8, 0), (0, 8), (16, 32), (32, 8), (24, 0)])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.base_speed = 5
        self.speed = self.base_speed
        self.love_points = 0
        self.angle = 0
        self.shield_active = False
        self.shield_timer = 0
        self.speed_boost_timer = 0
        self.magnet_timer = 0
        
    def apply_powerup(self, powerup_type):
        if powerup_type == 'speed':
            self.speed = self.base_speed * 2
            self.speed_boost_timer = 300  # 5 secondes à 60 FPS
        elif powerup_type == 'shield':
            self.shield_active = True
            self.shield_timer = 300
        elif powerup_type == 'magnet':
            self.magnet_timer = 300

    def update(self):
        # Mise à jour des timers
        if self.shield_timer > 0:
            self.shield_timer -= 1
            if self.shield_timer <= 0:
                self.shield_active = False
        
        if self.speed_boost_timer > 0:
            self.speed_boost_timer -= 1
            if self.speed_boost_timer <= 0:
                self.speed = self.base_speed
        
        if self.magnet_timer > 0:
            self.magnet_timer -= 1

        # Animation de rotation
        self.angle = (self.angle + 2) % 360
        self.image = pygame.transform.rotate(self.base_image, math.sin(math.radians(self.angle)) * 10)
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

        # Mouvement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Garder le joueur dans l'écran
        screen = pygame.display.get_surface()
        self.rect.clamp_ip(screen.get_rect())

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.shield_active:
            pygame.draw.circle(screen, (0, 0, 255, 128), self.rect.center, 
                             self.rect.width, 2)
