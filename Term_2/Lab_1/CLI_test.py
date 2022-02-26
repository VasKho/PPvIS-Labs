import argparse
import forest
import json
import random as rand


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'This is a program for life simulation')
    parser.add_argument('-s', '--skip', help = 'Pass some simulation steps')
    parser.add_argument('--animal', help = 'Create new animal {shark, parrotfish, barracuda}')
    parser.add_argument('--plant', nargs = 2, help = 'Create new plant')
    parser.add_argument('-p', '--print', nargs = '?', help = 'Print current forest state')

    args = parser.parse_args()


    field = forest.Ocean((20, 20))
    try:
        with open('./state.json', 'r') as area:
            info = json.loads(area.read())
            field = forest.parse_json(info)
            area.close()
    except FileNotFoundError:
        pass


    if args.skip:
        pass
    if args.animal:
        if args.animal == 'shark':
            animal = forest.Shark(100, 0)
            field.add_animal(animal, (rand.randrange(field.area[0]), rand.randrange(field.area[1])))
        elif args.animal == 'parrotfish':
            animal = forest.Parrotfish(100, 0)
            field.add_animal(animal, (rand.randrange(field.area[0]), rand.randrange(field.area[1])))
        elif args.animal == 'barracuda':
            animal = forest.Barracuda(100, 0)
            field.add_animal(animal, (rand.randrange(field.area[0]), rand.randrange(field.area[1])))
        else:
            print(f'Unknown animal name "{args.animal}"!')
    if args.plant:
        plant = forest.Plant(args.plant[0], args.plant[1])
        field.add_plant(plant, (rand.randrange(field.area[0]), rand.randrange(field.area[1])))
    if args.print:
        for animal, position in field.livings.items():
            print(animal, position)
        for plant, position in field.plants.items():
            print(plant, position)


    text = forest.convert_to_json(field)

    with open('./state.json', 'w') as area:
        area.truncate()
        area.write(text)
        area.close()
