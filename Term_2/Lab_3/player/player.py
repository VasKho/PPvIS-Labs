import pygame
import os
import time

from weapon.weapon import Weapon, Pistol, Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, **kwargs) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.angle = kwargs['angle']
        self.velocity = kwargs['velocity']
        self.weapon = list()
        for weapon in kwargs['weapon']:
            self.weapon.append(eval(weapon)())
        self.max_health = kwargs['max_health']
        self.position = {'x': pygame.display.Info().current_w//2, 'y': pygame.display.Info().current_h//2}
        self.current_weapon = self.weapon[-1]
        self.health = self.max_health
        self.score = 0

        img = pygame.image.load(os.path.abspath(kwargs['sprite_path'])).convert()
        img = pygame.transform.scale(img, (kwargs['scale'][0]*pygame.display.Info().current_w, kwargs['scale'][1]*pygame.display.Info().current_h))
        img.set_colorkey((0, 0, 0))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pygame.display.Info().current_w//2
        self.rect.y = pygame.display.Info().current_h//2


    def get_pos(self) -> tuple[int, int]:
        return (self.position['x'], self.position['y'])


    def move_up(self) -> bool:
        if self.position['y'] < 1.45*pygame.display.Info().current_h:
            self.position['y'] += self.velocity
            return True
        return False

    def move_down(self) -> bool:
        if self.position['y'] > -0.45*pygame.display.Info().current_h:
            self.position['y'] -= self.velocity
            return True
        return False

    def move_left(self) -> bool:
        if self.position['x'] < 1.47*pygame.display.Info().current_w:
            self.position['x'] += self.velocity
            return True
        return False

    def move_right(self) -> bool:
        if self.position['x'] > -0.47*pygame.display.Info().current_w:
            self.position['x'] -= self.velocity
            return True
        return False


    def get_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.kill()


    def up_score(self, score):
        self.score += score


    def rotate(self, key: str) -> None:
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


    def pickup_weapon(self, weapon: Weapon) -> None:
        self.weapon.append(weapon) 


    def shoot(self) -> Bullet:
        if time.time() > self.current_weapon.last_reload_time + self.current_weapon.reload_time: 
            self.current_weapon.reloading = False
        bullet = self.current_weapon.fire(self)
        self.current_weapon.reloading = True
        return bullet
    pass
