import pygame
import random
import math

class ParticleSystem:
    def __init__(self):
        self.particles = []
    
    def create_heart_particle(self, x, y, color=(255, 192, 203)):
        particle = {
            'x': x,
            'y': y,
            'size': random.randint(5, 10),
            'color': color,
            'life': 60,  # Durée de vie en frames
            'dx': random.uniform(-2, 2),
            'dy': random.uniform(-2, 0)
        }
        self.particles.append(particle)
    
    def update(self):
        for particle in self.particles[:]:
            particle['x'] += particle['dx']
            particle['y'] += particle['dy']
            particle['life'] -= 1
            if particle['life'] <= 0:
                self.particles.remove(particle)
    
    def draw(self, screen):
        for particle in self.particles:
            size = particle['size']
            x, y = int(particle['x']), int(particle['y'])
            alpha = min(255, particle['life'] * 4)
            surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            
            # Dessiner un petit cœur
            points = []
            for i in range(30):
                angle = (i / 30) * 2 * math.pi
                r = size * (1 - math.sin(angle))
                px = size + r * math.cos(angle)
                py = size + r * math.sin(angle)
                points.append((px, py))
            
            pygame.draw.polygon(surf, (*particle['color'], alpha), points)
            screen.blit(surf, (x - size, y - size))
