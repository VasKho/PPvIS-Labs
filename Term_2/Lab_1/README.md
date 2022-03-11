## About

This project is some kind of simulation of ocean life. It's written in Python and provides a CLI for work.

Here you can also find my first experience on OOP in Python.

## Usage

#### Requirements
* [argparse](https://pypi.org/project/argparse/) library.

#### Options
-s \<steps>, -\-skip \<steps> -- Pass some simulation steps
-\-animal {shark, parrotfish, barracuda} -- Create new animal
-\-plant \<lifespan> \<energy_value> -- Create new plant
-p, -\-print -- Print current ocean state

### State diagram

There is a diagram showing the common principles of animal behavior.

![State diagram](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/VasKho/PPvIS-Labs/master/Term_2/Lab_1/diagrams/state_diagram.puml)

### Config

As config file current program uses *state.json*. You may change it manually to specify some concrete situations.

## Modification

Class diagram below shows common structure of program. There are basic classes (initialized in *environment.py*):
* `Animal`,
* `Predator`,
* `Herbivorous`,
* `Food`,
* `Area`.

You can describe your own habitat inheriting your own animal classes from given one.

![Class diagram](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/VasKho/PPvIS-Labs/master/Term_2/Lab_1/diagrams/class_diagram.puml)
