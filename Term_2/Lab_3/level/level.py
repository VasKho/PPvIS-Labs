import pygame
from player.player import Player
from enemies.enemies import Enemy

class Level:
    def __init__(self, path_to_background):
        self.background = pygame.image.load(path_to_background).convert()
        self.background = pygame.transform.scale(self.background, (2*pygame.display.Info().current_w, 2*pygame.display.Info().current_h))
        self.rect = self.background.get_rect()
        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()


    def add_enemy(self, enemy: Enemy):
        self.enemies.add(enemy())
