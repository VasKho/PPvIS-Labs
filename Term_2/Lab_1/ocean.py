import environment as env
from random import randrange
import json
import curses

class Ocean(env.Area):
    pass


class Shark(env.Predator):
    def __init__(self, health: int, age: int, hunger: int = 100) -> None:
        env.Predator.__init__(self, health, age, 30, 60, False, hunger)

    def class_name(self) -> str:
        return 'shark'

    def reproduct(self):
        return Shark(100, 0)
    pass


class Parrotfish(env.Herbivorous):
    def __init__(self, health: int, age: int, hunger: int = 100) -> None:
        env.Herbivorous.__init__(self, health, age, 5, 20, False, hunger)

    def class_name(self) -> str:
        return 'parrotfish'
    
    def reproduct(self):
        return Parrotfish(100, 0)
    pass


class Barracuda(env.Predator):
    def __init__(self, health: int, age: int, hunger: int = 100) -> None:
        env.Predator.__init__(self, health, age, 30, 60, False, hunger)

    def class_name(self) -> str:
        return 'barracuda'

    def reproduct(self):
        return Barracuda(100, 0)
    pass


class Plant(env.Plant):
    pass


def parse_json(json_string: str) -> Ocean:
    text = json.loads(json_string)
    field = Ocean(text['area'])
    for animal in text['livings']:
        if animal["type"] == 'shark':
            shark = Shark(animal["health"], animal["age"], animal["hunger"])
            field.add_animal(shark, tuple(animal["position"]))
        elif animal["type"] == 'parrotfish':
            parrotfish = Parrotfish(animal["health"], animal["age"], animal["hunger"])
            field.add_animal(parrotfish, tuple(animal["position"]))
        elif animal["type"] == 'barracuda':
            barracuda = Barracuda(animal["health"], animal["age"], animal["hunger"])
            field.add_animal(barracuda, tuple(animal["position"]))
        else:
            print(f'Unknown animal name "{animal["type"]}!')

    for plant in text['plants']:
        tasty_plant = env.Plant(plant["lifespan"], plant["energy_value"])
        field.add_plant(tasty_plant, tuple(plant["position"]))
    return field


def convert_to_json(field: Ocean) -> str:
    text = dict()
    text.update({'area': field.area})
    animals = list()
    for animal, position in field.livings.items():
        animals.append({"type": animal.class_name(), "health": animal.health, "age": animal.age, "hunger": animal.hunger, "position": position})
    text.update({'livings': animals})
    plants = list()
    for plant, position in field.plants.items():
        plants.append({"lifespan": plant.lifespan, "energy_value": plant.energy_value, "position": position})
    text.update({'plants': plants})

    text = json.dumps(text, indent = 4, separators=(", ", ": "))
    return text


def add_animal(field: Ocean, animal_type: str):
    if animal_type == 'shark':
        animal = Shark(100, 0)
        field.add_animal(animal, (randrange(field.area[0]), randrange(field.area[1])))
    elif animal_type == 'parrotfish':
        animal = Parrotfish(100, 0)
        field.add_animal(animal, (randrange(field.area[0]), randrange(field.area[1])))
    elif animal_type == 'barracuda':
        animal = Barracuda(100, 0)
        field.add_animal(animal, (randrange(field.area[0]), randrange(field.area[1])))
    else:
        print(f'Unknown animal name "{animal_type}"!')


def add_plant(field: Ocean, lifespan: int, energy_value: int):
    plant = Plant(lifespan, energy_value)
    field.add_plant(plant, (randrange(field.area[0]), randrange(field.area[1])))


def skip(field: Ocean, number_of_steps: int):
    for _ in range(number_of_steps):
        dead_list = list()
        for instance in field.livings:
            instance.starve()
            direction = instance.move()
            if instance.death():
                dead_list.append(instance)
            else:
                if direction == 'up':
                    pos_list = list(field.livings[instance])
                    pos_list[1] = (pos_list[1] - 1) % (field.area[1] - 1)
                    field.livings[instance] = tuple(pos_list)
                elif direction == 'down':
                    pos_list = list(field.livings[instance])
                    pos_list[1] = (pos_list[1] + 1) % (field.area[1] - 1)
                    field.livings[instance] = tuple(pos_list)
                elif direction == 'left':
                    pos_list = list(field.livings[instance])
                    pos_list[0] = (pos_list[0] - 1) % (field.area[0] - 1)
                    field.livings[instance] = tuple(pos_list)
                elif direction == 'right':
                    pos_list = list(field.livings[instance])
                    pos_list[0] = (pos_list[0] + 1) % (field.area[0] - 1)
                    field.livings[instance] = tuple(pos_list)

        for animal in dead_list:
            del field.livings[animal]


def field_print(field: Ocean):
    stdscr = curses.initscr()
    curses.curs_set(0)
    for y in range(field.area[1]):
        for x in range(field.area[0]):
            stdscr.addstr(x, 2*y, '*')
    stdscr.addstr('\nPress any key to close...')

    for animal in field.livings:
        if animal.class_name() == 'shark':
            stdscr.addch(field.livings[animal][0], 2*field.livings[animal][1],'S')
        elif animal.class_name() == 'parrotfish':
            stdscr.addch(field.livings[animal][0], 2*field.livings[animal][1],'P')
        elif animal.class_name() == 'barracuda':
            stdscr.addch(field.livings[animal][0], 2*field.livings[animal][1],'B')

    for plant in field.plants:
        stdscr.addch(field.plants[plant][0], 2*field.plants[plant][1], '@')
    stdscr.refresh()
    stdscr.getch()
    curses.endwin()
