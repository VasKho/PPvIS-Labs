import pygame
from random import randrange
import glob
from abc import ABC, abstractclassmethod


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
            self.rect.x = randrange(0, pygame.display.Info().current_w)
            self.rect.y = randrange(0, pygame.display.Info().current_h)


    def update(self):
        if self.frame < len(self.images) - 1:
            self.frame += 1
        else: self.frame = 0
        self.image = self.images[self.frame]
    pass


class Antleredrascal(Enemy):
    def __init__(self):
        super().__init__("enemies/src/antleredrascalidle", 50)
    pass 


class Archfiend(Enemy):
    def __init__(self):
        super().__init__('enemies/src/archfiendidle', 30)
    pass


class Crimsonimp(Enemy):
    def __init__(self):
        super().__init__("enemies/src/crimsonimpidle", 30)
    pass


class Floatingeye(Enemy):
    def __init__(self):
        super().__init__("enemies/src/floatingeyeidle", 30)
    pass


class Glaringoverlord(Enemy):
    def __init__(self):
        super().__init__("enemies/src/glaringoverlordidle", 30)
    pass


class Grinninggremlin(Enemy):
    def __init__(self):
        super().__init__("enemies/src/grinninggremlinidle", 30)
    pass


class Hornedbrute(Enemy):
    def __init__(self):
        super().__init__("enemies/src/hornedbruteidle", 30)
    pass


class Pitbalor(Enemy):
    def __init__(self):
        super().__init__("enemies/src/pitbaloridle", 30)
    pass


class Skeweringstalker(Enemy):
    def __init__(self):
        super().__init__("enemies/src/skeweringstalkeridle", 30)
    pass


class Taintedscoundrel(Enemy):
    def __init__(self):
        super().__init__("enemies/src/taintedscoundrelidle", 30)
    pass
