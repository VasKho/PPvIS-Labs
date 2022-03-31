import os

from kivy.app import App
from kivy.app import Builder
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

import ui.dialogs as dialogs
import utils.parser as parser


class TableOutline(GridLayout):
    pass


class TableOutlineLabel(Label):
    pass


class Screen(RelativeLayout):
    table: TableOutline
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
        registry = parser.parse_file(os.path.join(path, filename[0]))
        for sportsman in registry:
            self.table.add_widget(TableOutlineLabel(text=sportsman.name))
            self.table.add_widget(TableOutlineLabel(text=sportsman.cast))
            self.table.add_widget(TableOutlineLabel(text=sportsman.position))
            self.table.add_widget(TableOutlineLabel(text=sportsman.title))
            self.table.add_widget(TableOutlineLabel(text=sportsman.sport))
            self.table.add_widget(TableOutlineLabel(text=sportsman.rank))
        self.dismiss_popup()


    def save(self, path, filename):
        self.dismiss_popup()


    def show_add(self):
        content = dialogs.AddNoteDialog(add=parser.write_to_xml, cancel=self.dismiss_popup)
        self._popup = dialogs.DialogPopup(title="Add note", content=content)
        self._popup.open()
    pass


class DatabaseApp(App):
    def build(self):
        screen = Screen()
        screen.table = TableOutline(pos_hint={'x': 0, 'top': 1})
        screen.add_widget(screen.table)
        return screen


Builder.load_file('./ui/sport.kv')
