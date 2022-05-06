import xml.sax as sax
from xml.sax import handler
from xml.dom import minidom


class ScoreTable:
    def __init__(self):
        self.fields = dict()


    def add(self, name: str, score: int) -> None:
        self.fields.update({str(name): int(score)})


    @staticmethod
    def read_from_xml(path: str=""):
        content: str
        if path == "":
            return None
        else:
            with open(path) as xml_file:
                content = xml_file.read()
        handler = ScoreTableHandler()
        sax.parseString(content, handler)
        return handler.table

        
    @staticmethod
    def write_to_xml(score_table, path: str):
        marklist = sorted(((value, key) for (key,value) in score_table.fields.items()), reverse=True)
        sortdict = dict([(k, v) for v, k in marklist])
        filtered_table = ScoreTable()
        for index, pair in enumerate(sortdict.items()):
            if index < 10:
                filtered_table.add(pair[0], pair[1])
        def create_field(dom: minidom.Document, tag_name: str, text) -> minidom.Element:
            tag = dom.createElement(tag_name)
            text_node = dom.createTextNode(text)
            tag.appendChild(text_node)
            return tag

        with open(path, mode="w") as xml_file:
            DOMTree = minidom.Document()
            table = DOMTree.createElement("score_table")
            for (key, value) in filtered_table.fields.items():
                player = DOMTree.createElement('player')
                player.appendChild(create_field(DOMTree, "name", key))
                player.appendChild(create_field(DOMTree, "score", str(value)))
                table.appendChild(player)
            DOMTree.appendChild(table)
            DOMTree.writexml(xml_file, addindent='\t', newl='\n', encoding="UTF-8")
    pass


class ScoreTableHandler(handler.ContentHandler):
    def __init__(self) -> None:
        self.table = ScoreTable()
        self.CurrentData = ""
        self.name = ""
        self.score = 0

    def startElement(self, tag, attributes):
        self.CurrentData = tag


    def endElement(self, tag):
        pass
        self.CurrentData = ""
        if tag == "player":
            self.table.add(name=self.name, score=self.score)
            self.name = ""
            self.score = 0


    def characters(self, content):
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "score":
            self.score = content
    pass
