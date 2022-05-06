import pygame
import yaml
import os
from math import sin, cos, radians
from abc import ABC, abstractclassmethod
import time
from random import choice


class Bullet(pygame.sprite.Sprite):
    def __init__(self, damage: int, bullet_image: str, velocity: int, angle: int, scale: tuple[int, int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.abspath(bullet_image)).convert()
        self.image = pygame.transform.scale(self.image, (scale[0]*pygame.display.Info().current_w, scale[1]*pygame.display.Info().current_h))
        self.image.set_colorkey((0, 0, 0))
        self.velocity = velocity
        self.angle = angle
        self.rect = self.image.get_rect()
        self.damage = damage
    

    def update(self) -> None:
        if self.rect.x in range(0, pygame.display.Info().current_w):
            self.rect.x += self.velocity * sin(radians(self.angle))
        else:
            self.kill()
        if self.rect.y in range(0, pygame.display.Info().current_h):
            self.rect.y += self.velocity * cos(radians(self.angle))
        else:
            self.kill()
    pass


class Weapon(ABC):
    def __init__(self, reload_time: float) -> None:
        self.reload_time = reload_time


    @abstractclassmethod
    def fire(self, owner):
        pass


class Shotgun(Weapon):
    def __init__(self) -> None:
        with open("weapon/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(conf['Shotgun']['reload_time'])
            self.damage = conf['Shotgun']['damage']
            self.bullet_image_path = conf['Shotgun']['bullet_image_path']
            self.bullet_velocity = conf['Shotgun']['bullet_velocity']
            self.image = pygame.image.load(conf['Shotgun']['weapon_image_path']).convert()
            self.image.set_colorkey((0, 0, 0))
            self.image = pygame.transform.scale(self.image, (\
                    conf['Shotgun']['weapon_scale'][0]*pygame.display.Info().current_w,\
                    conf['Shotgun']['weapon_scale'][1]*pygame.display.Info().current_h))
            self.bullet_scale = conf['Shotgun']['bullet_scale']
        self.reloading = False
        self.last_reload_time = time.time()


    def fire(self, owner):
        if not self.reloading:
            self.bullet = Bullet(self.damage, self.bullet_image_path, self.bullet_velocity, owner.angle, self.bullet_scale)
            self.bullet.rect = self.bullet.image.get_rect(center=(pygame.display.Info().current_w//2, pygame.display.Info().current_h//2))
            self.last_reload_time = time.time()
            return self.bullet
    pass


class Minigun(Weapon):
    def __init__(self) -> None:
        with open("weapon/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(conf['Minigun']['reload_time'])
            self.damage = conf['Minigun']['damage']
            self.bullet_image_path = conf['Minigun']['bullet_image_path']
            self.bullet_velocity = conf['Minigun']['bullet_velocity']
            self.image = pygame.image.load(conf['Minigun']['weapon_image_path']).convert()
            self.image.set_colorkey((0, 0, 0))
            self.image = pygame.transform.scale(self.image, (\
                    conf['Minigun']['weapon_scale'][0]*pygame.display.Info().current_w,\
                    conf['Minigun']['weapon_scale'][1]*pygame.display.Info().current_h))
            self.bullet_scale = conf['Minigun']['bullet_scale']
        self.reloading = False
        self.last_reload_time = time.time()


    def fire(self, owner):
        if not self.reloading:
            self.bullet = Bullet(self.damage, self.bullet_image_path, self.bullet_velocity, owner.angle, self.bullet_scale)
            normalize = choice([0, 5, 10])
            self.bullet.rect = self.bullet.image.get_rect(center=(pygame.display.Info().current_w//2+normalize, pygame.display.Info().current_h//2+normalize))
            self.last_reload_time = time.time()
            return self.bullet
    pass


class RBG(Weapon):
    def __init__(self) -> None:
        with open("weapon/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(conf['RBG']['reload_time'])
            self.damage = conf['RBG']['damage']
            self.bullet_image_path = conf['RBG']['bullet_image_path']
            self.bullet_velocity = conf['RBG']['bullet_velocity']
            self.image = pygame.image.load(conf['RBG']['weapon_image_path']).convert()
            self.image.set_colorkey((0, 0, 0))
            self.image = pygame.transform.scale(self.image, (\
                    conf['RBG']['weapon_scale'][0]*pygame.display.Info().current_w,\
                    conf['RBG']['weapon_scale'][1]*pygame.display.Info().current_h))
            self.bullet_scale = conf['RBG']['bullet_scale']
        self.reloading = False
        self.last_reload_time = time.time()


    def fire(self, owner):
        if not self.reloading:
            self.bullet = Bullet(self.damage, self.bullet_image_path, self.bullet_velocity, owner.angle, self.bullet_scale)
            self.bullet.rect = self.bullet.image.get_rect(center=(pygame.display.Info().current_w//2, pygame.display.Info().current_h//2))
            self.last_reload_time = time.time()
            return self.bullet
    pass
