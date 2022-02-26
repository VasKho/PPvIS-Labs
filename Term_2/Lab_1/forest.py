import environment as env
import json

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


def parse_json(text: dict) -> Ocean:
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
