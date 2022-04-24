import pygame
from menu.menu import Menu
from level.level import Level



pygame.init()
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


while True:
    menu = Menu(display)
    menu.run()
    del menu

    # for i in range(1, 21):
    #     level = Level(display, f"level/config/level{i}.yaml")
    #     level.start()
    #     del level
    level = Level(display, f"level/config/level1.yaml")
    level.start()
    del level
