import pygame
from player.player import Player
from enemies.enemies import Enemy


class Level:
    BACK_COLOR = (255, 200, 68)
    def __init__(self, path_to_background):
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.background = pygame.image.load(path_to_background).convert()
        self.background = pygame.transform.scale(self.background, (2*pygame.display.Info().current_w, 2*pygame.display.Info().current_h))
        self.rect = self.background.get_rect()

        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()


    def add_enemy(self, enemy: Enemy):
        self.enemies.add(enemy())


    def draw_player(self):
        player_rect = self.player.image.get_rect(center=(pygame.display.Info().current_w//2, pygame.display.Info().current_h//2))
        rot_image = pygame.transform.rotate(self.player.image, self.player.angle)
        rot_image_rect = rot_image.get_rect(center = player_rect.center)
        self.rect.center = self.player.get_pos()
        self.display.blit(rot_image, rot_image_rect.topleft)


    def update_background(self):
        self.display.blit(self.background, self.rect.topleft)


    def player_collide(self):
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.player.get_damage(enemy.damage)


    def bullet_collide(self):
        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    bullet.kill()
                    enemy.get_damage(bullet.damage)
                


    def update(self):
        player_rect = self.player.rect.topleft
        for en in self.enemies:
            en.trace(player_rect)

        self.display.fill(Level.BACK_COLOR)
        self.update_background()
        self.draw_player()

        self.bullets.update()
        self.bullets.draw(self.display)

        self.enemies.update()
        self.enemies.draw(self.display)

        self.player_collide()
        self.bullet_collide()

        pygame.display.update()
        self.clock.tick(40)
