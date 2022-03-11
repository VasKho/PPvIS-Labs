import environment as env
from random import randrange
import json
import curses
from itertools import combinations


class Ocean(env.Area):
    pass


class Shark(env.Predator):
    def __init__(self, health: int, age: int, hunger: int = 100) -> None:
        env.Predator.__init__(self, health, age, 30, 60, False, hunger)

    def class_name(self) -> str:
        return 'shark'

    def reproduct(self) -> 'Shark':
        return Shark(100, 0)
    pass


class Parrotfish(env.Herbivorous):
    def __init__(self, health: int, age: int, hunger: int = 100) -> None:
        env.Herbivorous.__init__(self, health, age, 5, 20, False, hunger)

    def class_name(self) -> str:
        return 'parrotfish'
    
    def reproduct(self) -> 'Parrotfish':
        return Parrotfish(100, 0)
    pass


class Barracuda(env.Predator):
    def __init__(self, health: int, age: int, hunger: int = 100) -> None:
        env.Predator.__init__(self, health, age, 30, 60, False, hunger)

    def class_name(self) -> str:
        return 'barracuda'

    def reproduct(self) -> 'Barracuda':
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
        # Make pairs from animal in same position
        pairs = list(combinations(field.livings, 2))
        pairs_cp = pairs.copy()
        for pair in pairs:
            if field.livings[pair[0]] != field.livings[pair[1]]:
                pairs_cp.remove(pair)

        pairs = pairs_cp
        # Feed them
        i = 0
        while i < len(pairs):
            if pairs[i][0].class_name() != pairs[i][1].class_name():
                if isinstance(pairs[i][0], env.Predator):
                    pairs[i][0].eat(pairs[i][1])
                    print(f'{pairs[i][1].class_name()} has been eaten by {pairs[i][0].class_name()}')
                    field.remove_animal(pairs[i][1])
                    pairs.remove(pairs[i])
                    i = 0
                    continue
                elif isinstance(pairs[i][1], env.Predator):
                    pairs[i][1].eat(pairs[i][0])
                    print(f'{pairs[i][0].class_name()} has been eaten by {pairs[i][1].class_name()}')
                    field.remove_animal(pairs[i][0])
                    pairs.remove(pairs[i])
                    i = 0
                    continue
            i += 1

        herbivorous_lst = [animal for animal in field.livings if isinstance(animal, env.Herbivorous)]
        plant_food = list(field.plants)
        for a in herbivorous_lst:
            edible = [plant for plant in plant_food if field.plants[plant] == field.livings[a]]
            if edible:
                a.eat(edible[0])
                field.remove_plant(edible[0])
                print(f'Plant has been eaten by {a.class_name()}')

        pairs = pairs_cp
        # Reproduction stuff
        for pair in pairs:
            if pair[0].class_name() == pair[1].class_name():
                field.add_animal(pair[0].reproduct(), field.livings[pair[0]])
                print(f'{pair[0].class_name()} was born')

        dead_list = []
        for animal in field.livings:
            if animal.death():
                dead_list.append(animal)

        for dead in dead_list:
            del field.livings[dead]
            print(f'{dead.class_name()} is dead.')

        for animal in field.livings:
            animal.starve()
            direction = animal.move()

            if direction == 'up':
                pos_list = list(field.livings[animal])
                pos_list[1] = (pos_list[1] - 1) % (field.area[1] - 1)
                field.livings[animal] = tuple(pos_list)
            elif direction == 'down':
                pos_list = list(field.livings[animal])
                pos_list[1] = (pos_list[1] + 1) % (field.area[1] - 1)
                field.livings[animal] = tuple(pos_list)
            elif direction == 'left':
                pos_list = list(field.livings[animal])
                pos_list[0] = (pos_list[0] - 1) % (field.area[0] - 1)
                field.livings[animal] = tuple(pos_list)
            elif direction == 'right':
                pos_list = list(field.livings[animal])
                pos_list[0] = (pos_list[0] + 1) % (field.area[0] - 1)
                field.livings[animal] = tuple(pos_list)

            print(f"{animal.class_name()} moved {direction}. New position is {field.livings[animal]}.")


def field_print(field: Ocean):
    stdscr = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)
    curses.init_pair(4, curses.COLOR_MAGENTA, -1)
    curses.init_pair(5, curses.COLOR_GREEN, -1)
    curses.curs_set(0)
    for y in range(field.area[1]):
        for x in range(field.area[0]):
            stdscr.addstr(x, 2*y, '*', curses.color_pair(1))
    stdscr.addstr('\nPress any key to close...')

    for animal in field.livings:
        if animal.class_name() == 'shark':
            stdscr.addch(field.livings[animal][0], 2*field.livings[animal][1],'S', curses.color_pair(2))
        elif animal.class_name() == 'parrotfish':
            stdscr.addch(field.livings[animal][0], 2*field.livings[animal][1],'P', curses.color_pair(3))
        elif animal.class_name() == 'barracuda':
            stdscr.addch(field.livings[animal][0], 2*field.livings[animal][1],'B', curses.color_pair(4))

    for plant in field.plants:
        stdscr.addch(field.plants[plant][0], 2*field.plants[plant][1], '@', curses.color_pair(5))
    stdscr.refresh()
    stdscr.getch()
    curses.endwin()
