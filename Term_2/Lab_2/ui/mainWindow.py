import os

from kivy.app import App
from kivy.app import Builder
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

import ui.dialogs as dialogs
import utils.context as context


class TableOutline(GridLayout):
    pass


class TableOutlineLabel(Label):
    pass


class Screen(RelativeLayout):
    table: TableOutline
    file = StringProperty(None)
    context = ObjectProperty(None)

    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.context = context.Context()


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


    def show_add(self):
        content = dialogs.AddNoteDialog(add=self.add, cancel=self.dismiss_popup)
        self._popup = dialogs.DialogPopup(title="Add note", content=content)
        self._popup.open()


    def show_delete(self):
        content = dialogs.DeleteNoteDialog(delete=self.delete, cancel=self.dismiss_popup)
        self._popup = dialogs.DialogPopup(title="Delete note", content=content)
        self._popup.open()


    def load(self, path, filename):
        self.file = os.path.join(path, filename[0])
        for widget in self.children:
            if isinstance(widget, TableOutline):
                self.remove_widget(widget)
        self.table = TableOutline()
        self.add_widget(self.table)
        self.context = context.Context(self.file)
        for sportsman in self.context.content:
            self.table.add_widget(TableOutlineLabel(text=sportsman.name))
            self.table.add_widget(TableOutlineLabel(text=sportsman.cast))
            self.table.add_widget(TableOutlineLabel(text=sportsman.position))
            self.table.add_widget(TableOutlineLabel(text=sportsman.title))
            self.table.add_widget(TableOutlineLabel(text=sportsman.sport))
            self.table.add_widget(TableOutlineLabel(text=sportsman.rank))
        self.dismiss_popup()


    def save(self, path, filename):
        self.context.save_context(os.path.join(path, filename))
        self.dismiss_popup()


    def add(self, name: str, cast: str, position: str, title: str, sport: str, rank: str):
        self.context.add_to_context(name, cast, position, title, sport, rank)
        self.table.add_widget(TableOutlineLabel(text=name))
        self.table.add_widget(TableOutlineLabel(text=cast))
        self.table.add_widget(TableOutlineLabel(text=position))
        self.table.add_widget(TableOutlineLabel(text=title))
        self.table.add_widget(TableOutlineLabel(text=sport))
        self.table.add_widget(TableOutlineLabel(text=rank))
        pass


    def delete(self):
        pass
    pass


class DatabaseApp(App):
    def build(self):
        screen = Screen()
        screen.table = TableOutline(pos_hint={'x': 0, 'top': 1})
        screen.add_widget(screen.table)
        return screen


Builder.load_file('./ui/sport.kv')
