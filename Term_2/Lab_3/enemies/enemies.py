import pygame
import yaml
from random import randrange, choice
import glob
from abc import ABC
from math import sqrt, sin, cos
import time


class Enemy(ABC, pygame.sprite.Sprite):
    def __init__(self, **kwargs) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0

        self.velocity = kwargs['velocity']
        self.health = kwargs['health']
        self.damage = kwargs['damage']
        self.change_direction_time = time.time()
        self.randomize_angle = 0

        for i in range(1, 41):
            current_image = [im for im in glob.glob(kwargs['path_to_image'] + '/*-' + str(i) + '.png')]
            img = pygame.image.load(current_image[0]).convert()
            img = pygame.transform.scale(img, (0.09*pygame.display.Info().current_w, 0.16*pygame.display.Info().current_h))
            img.set_colorkey((255, 255, 255))
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(randrange(0, pygame.display.Info().current_w), randrange(0, pygame.display.Info().current_h)))


    def trace(self, point: tuple[int, int]) -> None:
        vec_length = sqrt((point[0]-self.rect.x)**2 + (point[1]-self.rect.y)**2)
        if time.time() > self.change_direction_time + 1.5 and vec_length < 900:
            self.randomize_angle = choice([0, 90, 180, 270])
            self.change_direction_time = time.time()

        if vec_length < 10:
            return
        angle_sin = (point[1]-self.rect.y)/vec_length
        angle_cos = (point[0]-self.rect.x)/vec_length
        res_sin = angle_sin*cos(self.randomize_angle) + sin(self.randomize_angle)*angle_cos
        res_cos = angle_cos*cos(self.randomize_angle) - angle_sin*sin(self.randomize_angle)
        self.rect.move_ip(int(self.velocity*res_cos), int(self.velocity*res_sin))


    def get_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.kill()


    def update(self) -> None:
        if self.frame < len(self.images) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.image = self.images[self.frame]
    pass


class Goblin(Enemy):
    def __init__(self) -> None:
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Goblin'])
    pass 


class Archfiend(Enemy):
    def __init__(self) -> None:
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Archfiend'])
    pass


class Imp(Enemy):
    def __init__(self) -> None:
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Imp'])
    pass


class Floatingeye(Enemy):
    def __init__(self) -> None:
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Floatingeye'])
    pass


class Overlord(Enemy):
    def __init__(self) -> None:
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Overlord'])
    pass


class Gremlin(Enemy):
    def __init__(self) -> None:
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Gremlin'])
    pass


class Brute(Enemy):
    def __init__(self) -> None:
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Brute'])
    pass


class Pitbalor(Enemy):
    def __init__(self) -> None:
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Pitbalor'])
    pass


class Stalker(Enemy):
    def __init__(self) -> None: 
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Stalker'])
    pass


class Tainted(Enemy):
    def __init__(self) -> None:
        with open("enemies/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            super().__init__(**conf['Tainted'])
    pass
