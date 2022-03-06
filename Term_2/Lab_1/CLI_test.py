import argparse
import ocean


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'This is a program for life simulation')
    parser.add_argument('-s', '--skip', type = int, metavar = '<steps>', help = 'Pass some simulation steps')
    parser.add_argument('--animal', choices = ['shark', 'parrotfish', 'barracuda'], help = 'Create new animal')
    parser.add_argument('--plant', nargs = 2, type = int, metavar = ('<lifespan>', '<energy_value>'), help = 'Create new plant')
    parser.add_argument('-p', '--print', action = 'store_true', help = 'Print current ocean state')

    args = parser.parse_args()


    field = ocean.Ocean((20, 20))
    try:
        with open('./state.json', 'r') as area:
            field = ocean.parse_json(area.read())
            area.close()
    except FileNotFoundError:
        pass


    if args.skip:
        ocean.skip(field, args.skip)
    if args.animal:
        ocean.add_animal(field, args.animal)
    if args.plant:
        ocean.add_plant(field, args.plant[0], args.plant[1])
    if args.print:
        ocean.field_print(field)


    text = ocean.convert_to_json(field)

    with open('./state.json', 'w') as area:
        area.write(text)
        area.close()
