import pygame
import os
from random import randrange


class Antleredrascal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0
        self.velocity = 50

        for i in range(1, 41):
            img = pygame.image.load(os.path.abspath('enemies/src/antleredrascalidle/antleredrascalidle-' + str(i) + '.png')).convert()
            img = pygame.transform.scale(img, (0.09*pygame.display.Info().current_w, 0.16*pygame.display.Info().current_h))
            img.set_colorkey((255, 255, 255))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.rect.x = randrange(0, pygame.display.Info().current_w)
            self.rect.y = randrange(0, pygame.display.Info().current_h)


    def update(self):
        if self.frame < len(self.images) - 1:
            self.frame += 1
        else: self.frame = 0
        self.image = self.images[self.frame]
    pass 


class Archfiend(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0
        self.velocity = 30

        for i in range(1, 41):
            img = pygame.image.load(os.path.abspath('enemies/src/archfiendidle/archfiendidle-' + str(i) + '.png')).convert()
            img = pygame.transform.scale(img, (0.09*pygame.display.Info().current_w, 0.16*pygame.display.Info().current_h))
            img.set_colorkey((255, 255, 255))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.rect.x = randrange(0, pygame.display.Info().current_w)
            self.rect.y = randrange(0, pygame.display.Info().current_h)


    def update(self):
        if self.frame < len(self.images) - 1:
            self.frame += 1
        else: self.frame = 0
        self.image = self.images[self.frame]
    pass
