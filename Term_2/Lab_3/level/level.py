import pygame
import yaml
import random as rand
from level.map import Map
from enemies.enemies import (
        Goblin,
        Archfiend,
        Floatingeye,
        Imp,
        Overlord,
        Brute,
        Pitbalor,
        Stalker,
        Tainted,
        Gremlin
        )


class Level:
    def __init__(self, display: pygame.surface.Surface, conf_path: str):
        self.map = Map(display, conf_path)
        self.player = self.map.player
        self.num_of_enemies = 0
        with open(conf_path, 'r') as file:
            conf = yaml.safe_load(file)
            self.enemy_list = conf['enemies']
            self.max_number_of_enemies = conf['number_of_enemies']

        pygame.mixer.init()
        pygame.mixer.music.load('./soundtrack/game/doom.ogg')
        pygame.mixer.music.set_volume(0.7)


    def spawn_enemy(self):
        if self.num_of_enemies < self.max_number_of_enemies:
            en = eval(rand.choice(self.enemy_list))
            self.map.enemies.add(en())
            self.num_of_enemies += 1


    def start(self):
        pygame.mixer.music.play()


        pygame.mouse.set_visible(False)

        running = True

        while running:

            self.spawn_enemy()
            
            key_pressed_is = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        pygame.mouse.set_visible(True)
                        running = False

            if key_pressed_is[pygame.K_UP]:
                self.player.rotate('up')
            if key_pressed_is[pygame.K_DOWN]:
                self.player.rotate('down')
            if key_pressed_is[pygame.K_LEFT]:
                self.player.rotate('left')
            if key_pressed_is[pygame.K_RIGHT]:
                self.player.rotate('right')


            if key_pressed_is[pygame.K_SPACE]:
                bullet = self.player.shoot()
                if bullet is not None:
                    self.map.bullets.add(bullet)
               

            if key_pressed_is[pygame.K_w]:
                if self.player.move_up():
                    for enemy in self.map.enemies:
                        enemy.pos['y'] += self.player.velocity
            if key_pressed_is[pygame.K_s]:
                if self.player.move_down():
                    for enemy in self.map.enemies:
                        enemy.pos['y'] -= self.player.velocity
            if key_pressed_is[pygame.K_a]:
                if self.player.move_left():
                    for enemy in self.map.enemies:
                        enemy.pos['x'] += self.player.velocity
            if key_pressed_is[pygame.K_d]:
                if self.player.move_right():
                    for enemy in self.map.enemies:
                        enemy.pos['x'] -= self.player.velocity

            self.map.update()
            if len(self.map.enemies) == 0:
                pygame.mixer.music.stop()
                pygame.mouse.set_visible(True)
                return True

        return False
    pass
