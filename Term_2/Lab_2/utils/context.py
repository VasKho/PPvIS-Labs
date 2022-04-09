import utils.parser as parser

available_sports = parser.available_sports

class Context:
    def __init__(self, path: str='') -> None:
        if path == '':
            self.content = list()
        else:
            self.content = parser.parse_file(path)


    def add_to_context(self, name: str, cast: str, position: str, title: str, sport: str, rank: str):
        self.content.append(parser.Sportsman(name, cast, position, title, sport, rank))
        available_sports.add(sport)


    def delete_from_context(self, key: str, info: str) -> int:
        tag_name = ''
        if key == 'Имя':
            tag_name = 'name'
        elif key == 'Состав':
            tag_name = 'cast'
        elif key == 'Позиция':
            tag_name = 'position'
        elif key == 'Титул':
            tag_name = 'title'
        elif key == 'Вид спорта':
            tag_name = 'sport'
        elif key == 'Разряд':
            tag_name = 'rank'
        to_remove = []
        sport_counter = 0
        for i in self.content:
            if key == 'Вид спорта' and i.sport == key:
                sport_counter += 1
            if i.__dict__[tag_name] == info:
                to_remove.append(i)
        for i in to_remove:
            self.content.remove(i)
        if sport_counter == 0:
            available_sports.remove(info)
        return len(to_remove)


    def save_context(self, path: str):
        parser.write_to_xml(self.content, path)


    def find_in_context(self, key: str, info: str) -> list[parser.Sportsman]:
        tag_name = ''
        if key == 'Имя':
            tag_name = 'name'
        elif key == 'Состав':
            tag_name = 'cast'
        elif key == 'Позиция':
            tag_name = 'position'
        elif key == 'Титул':
            tag_name = 'title'
        elif key == 'Вид спорта':
            tag_name = 'sport'
        elif key == 'Разряд':
            tag_name = 'rank'
        found = []
        for i in self.content:
            if i.__dict__[tag_name] == info:
                found.append(i)
        return found
    pass
