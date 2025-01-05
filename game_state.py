import pygame
import random
from game.sprites.player import Player
from game.sprites.heart import Heart
from game.sprites.soulmate import Soulmate
from game.sprites.obstacle import Obstacle
from game.sprites.powerup import PowerUp
from game.particles import ParticleSystem

class GameState:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        
        self.player = Player(400, 500)
        self.soulmate = Soulmate(400, 100)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.soulmate)
        
        # Système de particules
        self.particle_system = ParticleSystem()
        
        # Ajouter les cœurs initiaux
        for _ in range(5):
            heart = Heart()
            self.hearts.add(heart)
            self.all_sprites.add(heart)
        
        # Ajouter les obstacles initiaux
        for _ in range(3):
            obstacle = Obstacle()
            self.obstacles.add(obstacle)
            self.all_sprites.add(obstacle)
        
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.victory = False
        self.score = 0
        
        # Chargement et lecture de la musique
        try:
            pygame.mixer.init()
            pygame.mixer.music.load("assets/music/romance.mp3")
            pygame.mixer.music.play(-1)  # -1 pour jouer en boucle
        except:
            print("Impossible de charger la musique")

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and (self.game_over or self.victory):
            if event.key == pygame.K_SPACE:
                self.__init__()

    def update(self):
        if not self.game_over and not self.victory:
            self.player.update()
            self.obstacles.update()
            self.particle_system.update()
            
            # Génération aléatoire de power-ups
            if random.random() < 0.002:  # 0.2% de chance par frame
                powerup = PowerUp()
                self.powerups.add(powerup)
                self.all_sprites.add(powerup)
            
            # Vérifier les collisions avec les obstacles
            if not self.player.shield_active:
                if pygame.sprite.spritecollide(self.player, self.obstacles, False):
                    self.game_over = True
            
            # Vérifier la collecte des cœurs
            hearts_collected = pygame.sprite.spritecollide(self.player, self.hearts, True)
            for heart in hearts_collected:
                self.player.love_points += 1
                self.score += 100
                # Ajouter des particules
                for _ in range(10):
                    self.particle_system.create_heart_particle(
                        heart.rect.centerx,
                        heart.rect.centery
                    )
                # Créer un nouveau cœur
                new_heart = Heart()
                self.hearts.add(new_heart)
                self.all_sprites.add(new_heart)
            
            # Vérifier la collecte des power-ups
            powerups_collected = pygame.sprite.spritecollide(self.player, self.powerups, True)
            for powerup in powerups_collected:
                self.player.apply_powerup(powerup.type)
                self.score += 50
            
            # Effet d'aimant
            if self.player.magnet_timer > 0:
                for heart in self.hearts:
                    dx = self.player.rect.centerx - heart.rect.centerx
                    dy = self.player.rect.centery - heart.rect.centery
                    dist = (dx * dx + dy * dy) ** 0.5
                    if dist < 200:  # Distance d'attraction
                        heart.rect.x += dx * 0.1
                        heart.rect.y += dy * 0.1
            
            # Vérifier la victoire
            if pygame.sprite.collide_rect(self.player, self.soulmate) and self.player.love_points >= 10:
                self.victory = True
                # Créer beaucoup de particules pour la victoire
                for _ in range(50):
                    self.particle_system.create_heart_particle(
                        self.player.rect.centerx,
                        self.player.rect.centery,
                        color=(255, 215, 0)  # Particules dorées
                    )

    def render(self, screen):
        screen.fill((0, 0, 225))  # Fond bleu
        
        # Dessiner les particules en premier (arrière-plan)
        self.particle_system.draw(screen)
        
        # Dessiner tous les sprites
        self.all_sprites.draw(screen)
        
        # Afficher le score et les points d'amour
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        love_text = self.font.render(f'Love Points: {self.player.love_points}/10', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(love_text, (10, 50))
        
        # Afficher les power-ups actifs
        if self.player.shield_active:
            shield_text = self.font.render('Shield Active!', True, (0, 0, 255))
            screen.blit(shield_text, (10, 90))
        if self.player.speed_boost_timer > 0:
            speed_text = self.font.render('Speed Boost!', True, (0, 255, 0))
            screen.blit(speed_text, (10, 130))
        if self.player.magnet_timer > 0:
            magnet_text = self.font.render('Love Magnet!', True, (128, 0, 128))
            screen.blit(magnet_text, (10, 170))
        
        if self.victory:
            victory_text = self.font.render('Love Wins! Press SPACE to play again', True, (255, 0, 150))
            screen.blit(victory_text, (200, 300))
        elif self.game_over:
            game_over_text = self.font.render('Game Over! Press SPACE to try again', True, (255, 0, 0))
            screen.blit(game_over_text, (200, 300))
