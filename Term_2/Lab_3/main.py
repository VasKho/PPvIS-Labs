import pygame
from player.player import Player
from enemies.enemies import (
        Antleredrascal,
        Archfiend,
        Floatingeye,
        Crimsonimp,
        Glaringoverlord,
        Hornedbrute,
        Pitbalor,
        Skeweringstalker,
        Taintedscoundrel,
        Grinninggremlin
        )


pygame.init()

level = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
pygame.display.set_caption('DOOM')

pygame.mixer.init()
pygame.mixer.music.load('./soundtrack/game/doom.ogg')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()

running = True

clock = pygame.time.Clock()

enemy_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()


slayer = Player()

antler = Antleredrascal()
enemy_list.add(antler)

arch = Archfiend()
enemy_list.add(arch)

crimson = Crimsonimp()
enemy_list.add(crimson)

floatingeye = Floatingeye()
enemy_list.add(floatingeye)

overlord = Glaringoverlord()
enemy_list.add(overlord)

horn = Hornedbrute()
enemy_list.add(horn)

pit = Pitbalor()
enemy_list.add(pit)

stalker = Skeweringstalker()
enemy_list.add(stalker)

scoundler = Taintedscoundrel()
enemy_list.add(scoundler)

gremlin = Grinninggremlin()
enemy_list.add(gremlin)
bullets = pygame.sprite.Group()


while running:
    clock.tick(40)


    level.fill((0, 0, 0))
    key_pressed_is = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if key_pressed_is[pygame.K_UP]:
        slayer.rotate('up')
    if key_pressed_is[pygame.K_DOWN]:
        slayer.rotate('down')
    if key_pressed_is[pygame.K_LEFT]:
        slayer.rotate('left')
    if key_pressed_is[pygame.K_RIGHT]:
        slayer.rotate('right')

    player_rect = slayer.image.get_rect(center=(slayer.position['x'], slayer.position['y']))
    # player_rect = slayer.image.get_rect(center=(pygame.display.Info().current_w//2, pygame.display.Info().current_h//2))
    rot_image = pygame.transform.rotate(slayer.image, slayer.angle)
    rot_image_rect = rot_image.get_rect(center = player_rect.center)
    level.fill((0, 0, 0))
    level.blit(rot_image, rot_image_rect.topleft)


    if key_pressed_is[pygame.K_SPACE]:
        bullet = slayer.shoot()
        if bullet is not None:
            bullets.add(bullet)
    bullets.update()
    bullets.draw(level)
        


    if key_pressed_is[pygame.K_w]:
        slayer.position['y'] -= slayer.velocity
    if key_pressed_is[pygame.K_s]:
        slayer.position['y'] += slayer.velocity
    if key_pressed_is[pygame.K_a]:
        slayer.position['x'] -= slayer.velocity
    if key_pressed_is[pygame.K_d]:
        slayer.position['x'] += slayer.velocity


    enemy_list.update()
    enemy_list.draw(level)

    pygame.display.update()
