import pygame
import os
import time

from weapon.weapon import Pistol


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 180
        self.velocity = 20
        self.position = {'x': pygame.display.Info().current_w//2, 'y': pygame.display.Info().current_h//2}
        self.weapon = [Pistol()]
        self.current_weapon = self.weapon[-1]

        img = pygame.image.load(os.path.abspath('player/src/marine.png')).convert()
        img = pygame.transform.scale(img, (0.09*pygame.display.Info().current_w, 0.16*pygame.display.Info().current_h))
        img.set_colorkey((255, 255, 255))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pygame.display.Info().current_w//2
        self.rect.y = pygame.display.Info().current_h//2


    def move_up(self):
        self.position['y'] += self.velocity

    def move_down(self):
        self.position['y'] -= self.velocity

    def move_left(self):
        self.position['x'] += self.velocity

    def move_right(self):
        self.position['x'] -= self.velocity


    def rotate(self, key: str):
        if key == 'up':
            if self.angle in range(0, 180):
                self.angle = (self.angle + 9) % 360
            elif self.angle in range(181, 360):
                self.angle = (self.angle - 9) % 360
        elif key == 'down':
            if self.angle in range(1, 180):
                self.angle = (self.angle - 9) % 360
            elif self.angle in range(181, 360):
                self.angle = (self.angle + 9) % 360
        elif key == 'left':
            if self.angle in range(90, 270):
                self.angle = (self.angle + 9) % 360
            elif self.angle in range(271, 360) or self.angle in range(0, 90):
                self.angle = (self.angle - 9) % 360
        elif key == 'right':
            if self.angle in range(91, 270):
                self.angle = (self.angle - 9) % 360
            elif self.angle in range(271, 360) or self.angle in range(0, 90):
                self.angle = (self.angle + 9) % 360


    def pickup_weapon(self, weapon):
        self.weapon.append(weapon) 


    def shoot(self):
        if time.time() > self.current_weapon.last_reload_time + self.current_weapon.reload_time: 
            self.current_weapon.reloading = False
        bullet = self.current_weapon.fire(self)
        self.current_weapon.reloading = True
        return bullet
    pass
