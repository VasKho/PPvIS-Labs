import re
import xml.sax as sax
from xml.sax import handler
from xml.dom import minidom


class Sportsman:
    def __init__(self) -> None:
        self.name = ""
        self.cast = ""
        self.position = ""
        self.title = ""
        self.sport = ""
        self.rank = ""
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


def write_to_xml(name: str, cast: str, position: str, title: str, sport: str, rank: str, path: str=""):
    def create_field(dom: minidom.Document, tag_name: str, text: str) -> minidom.Element:
        tag = dom.createElement(tag_name)
        text_node = dom.createTextNode(text)
        tag.appendChild(text_node)
        return tag

    try:
        with open(path, "r") as xml_file:
            content = xml_file.read()
            content = content.replace('\n', '')
            content = re.sub(r'\s{2,}', '', content)
            DOMTree = minidom.parseString(content)
    except FileNotFoundError:
        DOMTree = minidom.Document()
        pass
    registry = DOMTree.documentElement
    sportsman = DOMTree.createElement('sportsman')
    registry.appendChild(sportsman)
    sportsman.appendChild(create_field(DOMTree, "name", name))
    sportsman.appendChild(create_field(DOMTree, "cast", cast))
    sportsman.appendChild(create_field(DOMTree, "position", position))
    sportsman.appendChild(create_field(DOMTree, "title", title))
    sportsman.appendChild(create_field(DOMTree, "sport", sport))
    sportsman.appendChild(create_field(DOMTree, "rank", rank))
    DOMTree.normalize()
    with open(path, mode='w') as xml_file:
        DOMTree.writexml(xml_file, addindent='\t', newl='\n', encoding="UTF-8")
