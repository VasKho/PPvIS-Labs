import argparse
import forest
import json
import random as rand


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'This is a program for life simulation')
    parser.add_argument('-s', '--skip', help = 'Pass some simulation steps')
    parser.add_argument('--animal', help = 'Create new animal')
    parser.add_argument('--plant', help = 'Create new plant')

    args = parser.parse_args()


    field = forest.Forest((20, 20))
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
        if args.animal == 'bear':
            animal = forest.Bear(100, 0)
            field.add_animal(animal, (rand.randrange(field.area[0]), rand.randrange(field.area[1])))
    if args.plant:
        pass

    text = forest.convert_to_json(field)

    with open('./state.json', 'w') as area:
        area.truncate()
        area.write(text)
        area.close()
