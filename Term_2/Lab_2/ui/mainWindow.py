from kivy.app import App
from kivy.app import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

import ui.dialogs as dialogs
import utils.parser as parser


class Screen(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    context = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()


    def show_load(self):
        content = dialogs.DialogLoader(load=self.load, cancel=self.dismiss_popup)
        self._popup = dialogs.DialogPopup(title="Load file", content=content)
        self._popup.open()


    def show_save(self):
        content = dialogs.DialogSaver(save=self.save, cancel=self.dismiss_popup)
        self._popup = dialogs.DialogPopup(title="Save file", content=content)
        self._popup.open()


    def load(self, path, filename):
        os.path.join(path, filename[0]))
        self.dismiss_popup()


    def save(self, path, filename):
        # with open(os.path.join(path, filename), 'w') as stream:
        #     stream.write(self.context)
        self.dismiss_popup()


    def show_add(self):
        content = dialogs.AddNoteDialog(add=parser.write_to_xml, cancel=self.dismiss_popup)
        self._popup = dialogs.DialogPopup(title="Add note", content=content)
        self._popup.open()
    pass


class DatabaseApp(App):
    def build(self):
        return Screen()


Builder.load_file('./ui/sport.kv')
