import pytest
import pygame
from game.game_state import GameState

@pytest.fixture
def game_state():
    pygame.init()
    pygame.display.set_mode((800, 600))
    return GameState()

def test_player_movement(game_state):
    initial_x = game_state.player.x
    initial_y = game_state.player.y
    
    # Simule le mouvement vers la droite
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT}))
    game_state.update()
    assert game_state.player.x > initial_x
    
    # Simule le mouvement vers le bas
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_DOWN}))
    game_state.update()
    assert game_state.player.y > initial_y

