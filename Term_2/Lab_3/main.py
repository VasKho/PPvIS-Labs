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


pygame.mixer.init()
pygame.mixer.music.load('./soundtrack/game/doom.ogg')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()

running = True


level = Level("level/src/desert.jpg")
display = level.display
player = level.player

level.add_enemy(Goblin)
# level.add_enemy(Archfiend)
# level.add_enemy(Imp)
# level.add_enemy(Floatingeye)
# level.add_enemy(Overlord)
# level.add_enemy(Brute)
# level.add_enemy(Pitbalor)
# level.add_enemy(Stalker)
# level.add_enemy(Tainted)
# level.add_enemy(Gremlin)


while running:

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


    if key_pressed_is[pygame.K_SPACE]:
        bullet = player.shoot()
        if bullet is not None:
            level.bullets.add(bullet)
        


    if key_pressed_is[pygame.K_w]:
        if player.move_up():
            for enemy in level.enemies:
                enemy.pos['y'] += player.velocity
    if key_pressed_is[pygame.K_s]:
        if player.move_down():
            for enemy in level.enemies:
                enemy.pos['y'] -= player.velocity
    if key_pressed_is[pygame.K_a]:
        if player.move_left():
            for enemy in level.enemies:
                enemy.pos['x'] += player.velocity
    if key_pressed_is[pygame.K_d]:
        if player.move_right():
            for enemy in level.enemies:
                enemy.pos['x'] -= player.velocity


    level.update()
