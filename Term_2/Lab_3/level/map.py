import pygame
import yaml
from player.player import Player
from enemies.enemies import Enemy
from weapon.weapon import (
    Shotgun,
    Minigun,
    RBG
    )
import time
import pygame_menu
from menu.menu import MenuTheme


class Map:
    def __init__(self, display: pygame.surface.Surface, conf_path: str, score: int=0) -> None:
        with open(conf_path, 'r') as file:
            conf = yaml.safe_load(file)
            self.BACK_COLOR = pygame.Color(conf['back_color'])
            Map.FONT_COLOR = conf['font_color']
            self.background = pygame.image.load(conf['background_path']).convert()
            self.font_path = conf['font_path']
            self.font = pygame.font.Font(conf['font_path'], conf['font_size'])
            self.go_font = pygame.font.Font(conf['font_path'], 2*conf['font_size'])
            self.player = Player(**conf['Player'], score=score)

        self.clock = pygame.time.Clock()
        self.display = display

        self.background = pygame.transform.scale(self.background, (2*pygame.display.Info().current_w, 2*pygame.display.Info().current_h))
        self.rect = self.background.get_rect()

        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()


    def add_enemy(self, enemy: Enemy) -> None:
        self.enemies.add(enemy())


    def _draw_player(self) -> None:
        player_rect = self.player.image.get_rect(center=(pygame.display.Info().current_w//2, pygame.display.Info().current_h//2))
        rot_image = pygame.transform.rotate(self.player.image, self.player.angle)
        rot_image_rect = rot_image.get_rect(center = player_rect.center)
        self.rect.center = self.player.get_pos()
        self.display.blit(rot_image, rot_image_rect.topleft)


    def _draw_player_stats(self):
        percent = int(self.player.health/self.player.max_health * 100)
        health = self.font.render(str(percent) + '%', True, Map.FONT_COLOR)
        self.display.blit(health, (30, 30))
        pygame.draw.rect(self.display, (0,0,0), [20, 20, health.get_width()+20, health.get_height()+20], 2)
        score = self.font.render(str(self.player.score), True, Map.FONT_COLOR)
        self.display.blit(score, (pygame.display.Info().current_w//2+10, 30))
        pygame.draw.rect(self.display, (0,0,0), [pygame.display.Info().current_w//2, 30, score.get_width()+20, score.get_height()+20], 2)
        self.display.blit(self.player.current_weapon.image, (300, 20))


    def draw_game_over(self) -> None:
        go = self.go_font.render("EMOTIONAL DAMAGE", True, Map.FONT_COLOR)
        self.display.blit(go, (pygame.display.Info().current_w//2 - go.get_width()//2, pygame.display.Info().current_h//2 - go.get_height()//2))
        pygame.display.update()
        time.sleep(1)


    def get_input(self) -> str:
        self._player_name = None
        menu = pygame_menu.Menu('', 
                1000,
                400,
                theme=MenuTheme()
                )
        menu.set_title("Enter your name")
        menu.add.vertical_margin(30)

        def _write_input(Name):
            self._player_name = Name

        menu.add.text_input("Name: ", font_name=self.font_path, onchange=_write_input, maxchar=15)
        menu.add.vertical_fill()
        menu.add.button("Confirm", menu.disable)
        menu.add.vertical_margin(30)
        menu.mainloop(self.display, bgfun=self._draw_context)
        return self._player_name


    def _draw_context(self):
        self.display.fill(self.BACK_COLOR)
        self._update_background()
        self._draw_player()
        self._draw_player_stats()
        self.bullets.draw(self.display)
        self.enemies.draw(self.display)


    def _update_background(self) -> None:
        self.display.blit(self.background, self.rect.topleft)


    def _player_collide(self) -> None:
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.player.get_damage(enemy.damage)


    def _bullet_collide(self) -> None:
        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    bullet.kill()
                    if enemy.get_damage(bullet.damage):
                        self.player.up_score(enemy.score)


    def update(self) -> None:
        for en in self.enemies:
            if len(self.enemies) < 3:
                en.trace(self.player.rect.topleft, randomize=False)
            else:
                en.trace(self.player.rect.topleft)
            en.rect.clamp_ip(self.rect)
        self.bullets.update()
        self.enemies.update()
        # self._player_collide()
        self._bullet_collide()

        self._draw_context()

        pygame.display.update()
        self.clock.tick(40)
