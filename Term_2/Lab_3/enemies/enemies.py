import pygame
from random import randrange
import glob
from abc import ABC, abstractclassmethod
from math import sqrt


class Enemy(ABC, pygame.sprite.Sprite):
    @abstractclassmethod
    def __init__(self, path_to_image: str, velocity: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0
        self.velocity = velocity

        for i in range(1, 41):
            current_image = [im for im in glob.glob(path_to_image + '/*-' + str(i) + '.png')]
            img = pygame.image.load(current_image[0]).convert()
            img = pygame.transform.scale(img, (0.09*pygame.display.Info().current_w, 0.16*pygame.display.Info().current_h))
            img.set_colorkey((255, 255, 255))
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, 2*pygame.display.Info().current_w)
        self.rect.y = randrange(0, 2*pygame.display.Info().current_h)
        self.pos = {'x': self.rect.center[0], 'y': self.rect.center[1]}


    def trace(self, point: tuple[int, int]):
        vec_length = sqrt((point[0]-self.pos['x'])**2 + (point[1]-self.pos['y'])**2)
        if vec_length < 20:
            return
        angle_sin = (point[1]-self.pos['y'])/vec_length
        angle_cos = (point[0]-self.pos['x'])/vec_length
        self.pos['x'] += int(self.velocity*angle_cos)
        self.pos['y'] += int(self.velocity*angle_sin)
        self.rect = self.image.get_rect(center=(self.pos['x'], self.pos['y']))


    def update(self):
        if self.frame < len(self.images) - 1:
            self.frame += 1
        else: self.frame = 0
        self.image = self.images[self.frame]
    pass


class Goblin(Enemy):
    def __init__(self):
        super().__init__("enemies/src/goblin", 10)
    pass 


class Archfiend(Enemy):
    def __init__(self):
        super().__init__('enemies/src/archfiend', 13)
    pass


class Imp(Enemy):
    def __init__(self):
        super().__init__("enemies/src/imp", 19)
    pass


class Floatingeye(Enemy):
    def __init__(self):
        super().__init__("enemies/src/floatingeye", 5)
    pass


class Overlord(Enemy):
    def __init__(self):
        super().__init__("enemies/src/overlord", 15)
    pass


class Gremlin(Enemy):
    def __init__(self):
        super().__init__("enemies/src/gremlin", 17)
    pass


class Brute(Enemy):
    def __init__(self):
        super().__init__("enemies/src/brute", 17)
    pass


class Pitbalor(Enemy):
    def __init__(self):
        super().__init__("enemies/src/pitbalor", 14)
    pass


class Stalker(Enemy):
    def __init__(self):
        super().__init__("enemies/src/stalker", 16)
    pass


class Tainted(Enemy):
    def __init__(self):
        super().__init__("enemies/src/tainted", 13)
    pass
