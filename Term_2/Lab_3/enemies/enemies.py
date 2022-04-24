import pygame
import yaml
from random import randrange
import glob
from abc import ABC
from math import sqrt


class Enemy(ABC, pygame.sprite.Sprite):
    def __init__(self, **kwargs) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0

        self.velocity = kwargs['velocity']
        self.health = kwargs['health']
        self.damage = kwargs['damage']

        for i in range(1, 41):
            current_image = [im for im in glob.glob(kwargs['path_to_image'] + '/*-' + str(i) + '.png')]
            img = pygame.image.load(current_image[0]).convert()
            img = pygame.transform.scale(img, (0.09*pygame.display.Info().current_w, 0.16*pygame.display.Info().current_h))
            img.set_colorkey((255, 255, 255))
            self.images.append(img)
        self.image = self.images[0]
        self.pos = {'x': randrange(0, pygame.display.Info().current_w), 'y': randrange(0, pygame.display.Info().current_h)}
        self.rect = self.image.get_rect(center=(self.pos['x'], self.pos['y']))


    def trace(self, point: tuple[int, int]):
        vec_length = sqrt((point[0]-self.pos['x'])**2 + (point[1]-self.pos['y'])**2)
        if vec_length < 20:
            return
        angle_sin = (point[1]-self.pos['y'])/vec_length
        angle_cos = (point[0]-self.pos['x'])/vec_length
        self.pos['x'] += int(self.velocity*angle_cos)
        self.pos['y'] += int(self.velocity*angle_sin)
        image = self.images[self.frame]
        self.rect = image.get_rect(center=(self.pos['x'], self.pos['y']))


    def get_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()


    def update(self):
        if self.frame < len(self.images) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center=(self.pos['x'], self.pos['y']))
    pass


class Goblin(Enemy):
    def __init__(self):
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Goblin'])
    pass 


class Archfiend(Enemy):
    def __init__(self):
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Archfiend'])
    pass


class Imp(Enemy):
    def __init__(self):
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Imp'])
    pass


class Floatingeye(Enemy):
    def __init__(self):
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Floatingeye'])
    pass


class Overlord(Enemy):
    def __init__(self):
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Overlord'])
    pass


class Gremlin(Enemy):
    def __init__(self):
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Gremlin'])
    pass


class Brute(Enemy):
    def __init__(self):
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Brute'])
    pass


class Pitbalor(Enemy):
    def __init__(self):
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Pitbalor'])
    pass


class Stalker(Enemy):
    def __init__(self): 
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Stalker'])
    pass


class Tainted(Enemy):
    def __init__(self):
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Tainted'])
    pass
