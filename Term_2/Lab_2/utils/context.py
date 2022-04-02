import utils.parser as parser

class Context:
    def __init__(self, path: str="") -> None:
        if path == "":
            self.content = list()
        else:
            self.content = parser.parse_file(path)


    def add_to_context(self, name: str, cast: str, position: str, title: str, sport: str, rank: str):
        self.content.append(parser.Sportsman(name, cast, position, title, sport, rank))


    def delete_from_context(self, tag_name: str, info: str):
        to_remove = []
        for i in self.content:
            if i.__dict__[tag_name] == info:
                to_remove.append(i)
        for i in to_remove:
            self.content.remove(i)


    def save_context(self, path: str):
        parser.write_to_xml(self.content, path)
    pass
