import pygame 
import sys
from game.game_state import GameState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mon Jeu")
        self.clock = pygame.time.Clock()
        self.game_state = GameState()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self.game_state.handle_event(event)
        return True

    def update(self):
        self.game_state.update()

    def render(self):
        self.screen.fill((0, 0, 0))  # Fond noir
        self.game_state.render(self.screen)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # 60 FPS

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

