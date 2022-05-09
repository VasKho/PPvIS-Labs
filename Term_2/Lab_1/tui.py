import pygame
import pygame_menu
import ocean
from itertools import product


def draw_field():
    for x, y in product(range(field.area[0]), range(field.area[1])):
        image = pygame_menu.baseimage.BaseImage("/home/vaskho/Study/PPvIS-Labs/Term_2/Lab_1/img/back.png")
        image.scale(0.2, 0.2)
        table.get_cell(x+1, y+1).set_image(image)
    for animal in field.livings:
        cell = table.get_cell(field.livings[animal][0]+1, field.livings[animal][1]+1)
        if animal.class_name() == "shark":
            image = pygame_menu.baseimage.BaseImage("/home/vaskho/Study/PPvIS-Labs/Term_2/Lab_1/img/shark.png")
            image.scale(0.2, 0.2)
            cell.set_image(image)
        elif animal.class_name() == "parrotfish":
            image = pygame_menu.baseimage.BaseImage("/home/vaskho/Study/PPvIS-Labs/Term_2/Lab_1/img/parrotfish.png")
            image.scale(0.118, 0.118)
            cell.set_image(image)
        elif animal.class_name() == "barracuda":
            image = pygame_menu.baseimage.BaseImage("/home/vaskho/Study/PPvIS-Labs/Term_2/Lab_1/img/barracuda.png")
            image.scale(0.092, 0.1)
            cell.set_image(image)

    for plant in field.plants:
        cell = table.get_cell(field.plants[plant][0]+1, field.plants[plant][1]+1)
        image = pygame_menu.baseimage.BaseImage("/home/vaskho/Study/PPvIS-Labs/Term_2/Lab_1/img/grass.png")
        image.scale(0.035, 0.035)
        cell.set_image(image)


def next(field: ocean.Ocean, number_of_steps: int):
    ocean.skip(field, number_of_steps)
    draw_field()


def add(field: ocean.Ocean, type: str):
    if type != "plant":
        ocean.add_animal(field, type)
    else:
        ocean.add_plant(field, 10, 30)
    draw_field()


pygame.init()
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

field = ocean.Ocean((20, 20))
try:
    with open('./state.json', 'r') as area:
        field = ocean.parse_json(area.read())
        area.close()
except FileNotFoundError:
    pass

menu = pygame_menu.Menu('',
        pygame.display.Info().current_w,
        pygame.display.Info().current_h,
        theme=pygame_menu.themes.THEME_DARK,
        columns=4,
        rows=2
        )

table = menu.add.table()
table.resize(width=60, height = 60)

for y in range(field.area[1]):
    row = list()
    for x in range(field.area[0]):
        row.append(pygame_menu.widgets.Image("./img/back.png", scale=(0.2, 0.2)))
    table.add_row(row, cell_align=pygame_menu.locals.ALIGN_CENTER, cell_border_width=0)

menu.add.button("Next", next, field, 1)
menu.add.button("Add shark", add, field, "shark")
menu.add.button("Add parrotfish", add, field, "parrotfish")
menu.add.button("Add barracuda", add, field, "barracuda")
menu.add.button("Add plant", add, field, "plant")
menu.add.button("Exit", menu.disable)

menu.mainloop(display, bgfun=draw_field)
