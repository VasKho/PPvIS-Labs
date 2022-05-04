import pygame
from menu.menu import Menu
from level.level import Level, DEATH, PASS


def start_game():
    level_number = 1
    while level_number < max_levels:
        if level_number == 1:
            level = Level(display, "level/config/level1.yaml")
            level.start()
        for event in pygame.event.get():
            if event.type == DEATH:
                return
            if event.type == PASS:
                level_number += 1
                level = Level(display, f"level/config/level{level_number}.yaml", event.score)
                level.start()

pygame.init()
max_levels = 3
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
menu = Menu(display, start=start_game, show_score=None, help=None)
menu.run()
