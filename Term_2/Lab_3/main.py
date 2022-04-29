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
level = Level(display, f"level/config/level1.yaml")
player = level.start()

while True:
    for i in range(2, max_levels+1):
        if player:
            level = Level(display, f"level/config/level{i}.yaml", player)
        else:
            break
        player = level.start()
    show_menu()
