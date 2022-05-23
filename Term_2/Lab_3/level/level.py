import score_table.score as st
import threading
import pygame
import yaml
import random as rand
from level.map import Map
from player.player import Player
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


DEATH = pygame.USEREVENT + 0
PASS = pygame.USEREVENT + 1


class Level:
    def __init__(self, display: pygame.surface.Surface, conf_path: str, score: int=0) -> None:
        self.map = Map(display, conf_path, score)
        self.player = self.map.player
        self.num_of_enemies = 0
        with open(conf_path, 'r') as file:
            conf = yaml.safe_load(file)
            self.enemy_list = conf['enemies']
            self.max_number_of_enemies = conf['number_of_enemies']


    def spawn_enemy(self) -> None:
        en = eval(rand.choice(self.enemy_list))
        enemy_object = en()
        self.map.enemies.add(enemy_object)


    def start(self):
        pygame.mouse.set_visible(False)

        spawn = threading.Thread(target=self.spawn_enemy)
        spawn.start()
        self.num_of_enemies += 1
        spawn.join()

        running = True
        while running:

            key_pressed_is = pygame.key.get_pressed()

            if self.num_of_enemies < self.max_number_of_enemies:
                threading.Thread(target=self.spawn_enemy).start()
                self.num_of_enemies += 1

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
                        enemy.rect.move_ip(0, self.player.velocity)
            if key_pressed_is[pygame.K_s]:
                if self.player.move_down():
                    for enemy in self.map.enemies:
                        enemy.rect.move_ip(0, -self.player.velocity)
            if key_pressed_is[pygame.K_a]:
                if self.player.move_left():
                    for enemy in self.map.enemies:
                        enemy.rect.move_ip(self.player.velocity, 0)
            if key_pressed_is[pygame.K_d]:
                if self.player.move_right():
                    for enemy in self.map.enemies:
                        enemy.rect.move_ip(-self.player.velocity, 0)

            if key_pressed_is[pygame.K_1]:
                self.player.change_weapon(0)
            if key_pressed_is[pygame.K_2]:
                self.player.change_weapon(1)
            if key_pressed_is[pygame.K_3]:
                self.player.change_weapon(2)

            if len(self.map.player_group) == 0:
                self.map.draw_game_over()
                pygame.mouse.set_visible(True)
                pygame.mixer.music.stop()
                score_table = st.ScoreTable.read_from_xml("score_table/score_table.xml")
                name = self.map.get_input()
                if name:
                    score_table.add(name=name, score=self.player.score)
                else: 
                    score_table.add(name="Unknown", score=self.player.score)
                st.ScoreTable.write_to_xml(score_table, "score_table/score_table.xml")
                break


            self.map.update()
            if len(self.map.enemies) == 0:
                pygame.mouse.set_visible(True)
                pygame.event.post(pygame.event.Event(PASS, score=self.player.score))
                return

        pygame.event.post(pygame.event.Event(DEATH, score=self.player.score))
    pass
