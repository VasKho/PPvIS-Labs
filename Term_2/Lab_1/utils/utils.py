import pygame
import pygame_menu
import ocean

def next(field: ocean.Ocean, number_of_steps: int, update_callback):
    ocean.skip(field, number_of_steps)
    update_callback()

def add(field: ocean.Ocean, type: str, update_callback):
    if type != "plant":
        ocean.add_animal(field, type)
    else:
        ocean.add_plant(field, 10, 30)
    update_callback()