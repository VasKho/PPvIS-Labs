import pygame
from menu.menu import Menu
from level.level import Level


def show_menu() -> None:
    menu = Menu(display)
    menu.run()
    del menu


pygame.init()
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

level_number = 1
max_levels = 2

show_menu()

while True:
    level = Level(display, f"level/config/level{level_number}.yaml")
    if level.start():
        del level
        if level_number < max_levels:
            level_number += 1
            level = Level(display, f"level/config/level{level_number}.yaml")
        else:
            level_number = 1
            show_menu()
    else:
        del level
        show_menu()
