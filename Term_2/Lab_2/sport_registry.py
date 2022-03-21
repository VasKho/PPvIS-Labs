from kivy.app import App
from kivy.app import Builder
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

import os
import dialogs
from xml.dom import minidom


class DialogPopup(Popup):
    pass


class Screen(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    context = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()


    def show_load(self):
        content = dialogs.DialogLoader(load=self.load, cancel=self.dismiss_popup)
        self._popup = DialogPopup(title="Load file", content=content)
        self._popup.open()


    def show_save(self):
        content = dialogs.DialogSaver(save=self.save, cancel=self.dismiss_popup)
        self._popup = DialogPopup(title="Save file", content=content)
        self._popup.open()


    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.context = stream.read()
        self.dismiss_popup()


    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.context)
        self.dismiss_popup()
    pass


class DatabaseApp(App):
    def build(self):
        return Screen()


Builder.load_file('./config/sport.kv')


if __name__ == '__main__':
    DatabaseApp().run()
