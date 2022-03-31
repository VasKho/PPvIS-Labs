from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


class DialogPopup(Popup):
    pass


class DialogLoader(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    pass


class DialogSaver(FloatLayout):
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)
    pass


class AddNoteDialog(FloatLayout):
    add = ObjectProperty(None)
    cancel = ObjectProperty(None)
    pass


class DeleteNoteDialog(FloatLayout):
    delete = ObjectProperty(None)
    cancel = ObjectProperty(None)
    pass
