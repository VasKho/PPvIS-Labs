import xml.sax as sax
from xml.sax import handler
from xml.dom import minidom


class Sportsman:
    def __init__(self, name: str='', cast: str='', position: str='', title: str='', sport: str='', rank: str='') -> None:
        self.name = name
        self.cast = cast
        self.position = position
        self.title = title
        self.sport = sport
        self.rank = rank
    pass


class RegistryHandler(handler.ContentHandler):
    def __init__(self) -> None:
        self.registry = list()
        self.CurrentData = ""
        self.name = ""
        self.cast = ""
        self.position = ""
        self.title = ""
        self.sport = ""
        self.rank = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "sportsman":
            self.registry.append(Sportsman())


    def endElement(self, tag):
        self.CurrentData = ""


    def characters(self, content):
        if self.CurrentData == "name":
            self.registry[-1].name = content
        elif self.CurrentData == "cast":
            self.registry[-1].cast = content
        elif self.CurrentData == "position":
            self.registry[-1].position = content
        elif self.CurrentData == "title":
            self.registry[-1].title = content
        elif self.CurrentData == "sport":
            self.registry[-1].sport = content
        elif self.CurrentData == "rank":
            self.registry[-1].rank = content
    pass


def parse_file(path: str="") -> list[Sportsman]:
    content: str
    if path == "":
        return []
    else:
        with open(path) as xml_file:
            content = xml_file.read()
    reg_handler = RegistryHandler()
    sax.parseString(content, reg_handler)
    return reg_handler.registry


def write_to_xml(sportsmans: list[Sportsman], path: str):
    def create_field(dom: minidom.Document, tag_name: str, text) -> minidom.Element:
        tag = dom.createElement(tag_name)
        text_node = dom.createTextNode(text)
        tag.appendChild(text_node)
        return tag

    with open(path, mode="w") as xml_file:
        DOMTree = minidom.Document()
        registry = DOMTree.createElement("registry")
        for i in sportsmans:
            sportsman = DOMTree.createElement('sportsman')
            sportsman.appendChild(create_field(DOMTree, "name", i.name))
            sportsman.appendChild(create_field(DOMTree, "cast", i.cast))
            sportsman.appendChild(create_field(DOMTree, "position", i.position))
            sportsman.appendChild(create_field(DOMTree, "title", i.title))
            sportsman.appendChild(create_field(DOMTree, "sport", i.sport))
            sportsman.appendChild(create_field(DOMTree, "rank", i.rank))
            registry.appendChild(sportsman)
        DOMTree.appendChild(registry)
        DOMTree.writexml(xml_file, addindent='\t', newl='\n', encoding="UTF-8")
