import pygame
import model.ocean as ocean
import ui.ui as ui

pygame.init()
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

field = ocean.Ocean((20, 20))

try:
    with open('./state.json', 'r') as area:
        field = ocean.parse_json(area.read())
        area.close()
except FileNotFoundError:
    pass

menu = ui.Ui(field)

menu.run_ui(display)

text = ocean.convert_to_json(field)

with open('./state.json', 'w') as area:
    area.write(text)
    area.close()