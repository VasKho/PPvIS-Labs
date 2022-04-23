import pygame
import os
from math import sin, cos, radians
from abc import ABC, abstractclassmethod
import time


class Bullet(pygame.sprite.Sprite):
    def __init__(self, damage, bullet_image, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.abspath(bullet_image)).convert()
        self.image = pygame.transform.scale(self.image, (0.01*pygame.display.Info().current_w, 0.01*pygame.display.Info().current_h))
        self.image.set_colorkey((255, 255, 255))
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.rect = self.image.get_rect()
        self.damage = damage
    

    def update(self):
        if self.rect.x in range(0, pygame.display.Info().current_w):
            self.rect.x += self.vel_x
        else:
            self.kill()
        if self.rect.y in range(0, pygame.display.Info().current_h):
            self.rect.y += self.vel_y
        else:
            self.kill()
    pass


class Weapon(ABC):
    @abstractclassmethod
    def __init__(self, reload_time) -> None:
        self.reload_time = reload_time


    @abstractclassmethod
    def fire(self, owner):
        pass


class Pistol(Weapon):
    def __init__(self) -> None:
        super().__init__(0.5)
        self.reloading = False
        self.last_reload_time = time.time()


    def fire(self, owner):
        if not self.reloading:
            self.bullet = Bullet(10, "./weapon/src/bullet.png", 30*sin(radians(owner.angle)), 30*cos(radians(owner.angle)))
            self.bullet.rect = self.bullet.image.get_rect(center=(pygame.display.Info().current_w//2, pygame.display.Info().current_h//2))
            self.last_reload_time = time.time()
            return self.bullet
    pass
