import pygame
from level.level import Level
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


pygame.init()


display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
pygame.display.set_caption('DOOM')

pygame.mixer.init()
pygame.mixer.music.load('./soundtrack/game/doom.ogg')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()

running = True

clock = pygame.time.Clock()


level = Level("level/src/desert.jpg")
player = level.player


level.add_enemy(Goblin)
level.add_enemy(Archfiend)
level.add_enemy(Imp)
level.add_enemy(Floatingeye)
level.add_enemy(Overlord)
level.add_enemy(Brute)
level.add_enemy(Pitbalor)
level.add_enemy(Stalker)
level.add_enemy(Tainted)
level.add_enemy(Gremlin)


while running:
    clock.tick(40)


    key_pressed_is = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if key_pressed_is[pygame.K_UP]:
        player.rotate('up')
    if key_pressed_is[pygame.K_DOWN]:
        player.rotate('down')
    if key_pressed_is[pygame.K_LEFT]:
        player.rotate('left')
    if key_pressed_is[pygame.K_RIGHT]:
        player.rotate('right')

    # player_rect = slayer.image.get_rect(center=(slayer.position['x'], slayer.position['y']))
    player_rect = player.image.get_rect(center=(pygame.display.Info().current_w//2, pygame.display.Info().current_h//2))
    rot_image = pygame.transform.rotate(player.image, player.angle)
    rot_image_rect = rot_image.get_rect(center = player_rect.center)
    level.rect.center = (player.position['x'], player.position['y'])
    display.fill((0, 0, 0))
    display.blit(level.background, level.rect.topleft)
    display.blit(rot_image, rot_image_rect.topleft)


    if key_pressed_is[pygame.K_SPACE]:
        bullet = player.shoot()
        if bullet is not None:
            level.bullets.add(bullet)
    level.bullets.update()
    level.bullets.draw(display)
        


    if key_pressed_is[pygame.K_w]:
        player.move_up()
    if key_pressed_is[pygame.K_s]:
        player.move_down()
    if key_pressed_is[pygame.K_a]:
        player.move_left()
    if key_pressed_is[pygame.K_d]:
        player.move_right()


    level.enemies.update()
    level.enemies.draw(display)

    pygame.display.update()
