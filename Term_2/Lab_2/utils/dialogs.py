from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


class DialogLoader(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    pass


class DialogSaver(FloatLayout):
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)
    pass


class AddNoteDialog(FloatLayout):
    pass

class DeleteNoteDialog(FloatLayout):
    pass
