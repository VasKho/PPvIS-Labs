import pygame
import yaml
from player.player import Player
from enemies.enemies import Enemy
from weapon.weapon import (
    Pistol,
    Shotgun
    )
import time


class Map:
    def __init__(self, display: pygame.surface.Surface, conf_path: str, score: int=0) -> None:
        with open(conf_path, 'r') as file:
            conf = yaml.safe_load(file)
            self.BACK_COLOR = pygame.Color(conf['back_color'])
            Map.FONT_COLOR = conf['font_color']
            self.background = pygame.image.load(conf['background_path']).convert()
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


    def draw_player(self) -> None:
        player_rect = self.player.image.get_rect(center=(pygame.display.Info().current_w//2, pygame.display.Info().current_h//2))
        rot_image = pygame.transform.rotate(self.player.image, self.player.angle)
        rot_image_rect = rot_image.get_rect(center = player_rect.center)
        self.rect.center = self.player.get_pos()
        self.display.blit(rot_image, rot_image_rect.topleft)


    def draw_player_stats(self):
        percent = int(self.player.health/self.player.max_health * 100)
        health = self.font.render(str(percent) + '%', True, Map.FONT_COLOR)
        self.display.blit(health, (30, 30))
        pygame.draw.rect(self.display, (0,0,0), [20, 20, health.get_width()+20, health.get_height()+20], 2)
        score = self.font.render(str(self.player.score), True, Map.FONT_COLOR)
        self.display.blit(score, (pygame.display.Info().current_w//2+10, 30))
        pygame.draw.rect(self.display, (0,0,0), [pygame.display.Info().current_w//2, 30, score.get_width()+20, score.get_height()+20], 2)


    def draw_game_over(self) -> None:
        go = self.go_font.render("YOU DIED", True, Map.FONT_COLOR)
        self.display.blit(go, (pygame.display.Info().current_w//2 - go.get_width()//2, pygame.display.Info().current_h//2 - go.get_height()//2))
        pygame.display.update()
        time.sleep(1)


    def update_background(self) -> None:
        self.display.blit(self.background, self.rect.topleft)


    def player_collide(self) -> None:
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.player.get_damage(enemy.damage)


    def bullet_collide(self) -> None:
        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    bullet.kill()
                    if enemy.get_damage(bullet.damage):
                        self.player.up_score(enemy.score)
                    # enemy.kill()


    def update(self) -> None:
        for en in self.enemies:
            en.trace(self.player.rect.topleft)
            en.rect.clamp_ip(self.rect)

        self.display.fill(self.BACK_COLOR)
        self.update_background()
        self.draw_player()
        self.draw_player_stats()

        self.bullets.update()
        self.bullets.draw(self.display)

        self.enemies.update()
        self.enemies.draw(self.display)

        # self.player_collide()
        self.bullet_collide()

        pygame.display.update()
        self.clock.tick(40)
