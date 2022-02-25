import environment as env
import json

class Forest(env.Area):
    pass


class Bear(env.Predator):
    def __init__(self, health: int, age: int, hunger: int = 100) -> None:
        env.Predator.__init__(self, health, age, 30, 60, False, hunger)

    def class_name(self) -> str:
        return 'bear'

    def reproduct(self):
        return Bear(100, 0)
    pass

class Bunny(env.Herbivorous):
    def __init__(self, health: int, age: int) -> None:
        env.Herbivorous.__init__(self, health, age, 5, 20, False)

    def class_name(self) -> str:
        return 'bunny'
    
    def reproduct(self):
        return Bunny(100, 0)
    pass


def parse_json(text: dict) -> Forest:
    field = Forest(text['area'])
    for animal in text['livings']:
        if animal[0] == 'bear':
            bear = Bear(animal[1], animal[2], animal[3])
            field.add_animal(bear, tuple(animal[4]))
    for plant in text['plants']:
        tasty_plant = env.Plant(plant[0], plant[1])
        field.add_plant(tasty_plant, tuple(plant[2]))
    return field


def convert_to_json(field: Forest) -> str:
    text = dict()
    text.update({'area': field.area})
    animals = list()
    for animal, position in field.livings.items():
        animals.append((animal.class_name(), animal.health, animal.age, animal.hunger, position))
    text.update({'livings': animals})
    plants = list()
    for plant, position in field.plants.items():
        plants.append((plant.lifespan, plant.energy_value, position))
    text.update({'plants': plants})

    text = json.dumps(text, indent = 4, separators=(", ", ": "))
    return text
