import os
from math import floor

from kivy.app import App
from kivy.app import Builder
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

import ui.dialogs as dialogs
import utils.context as context


class TableOutline(GridLayout):
    pass


class TableOutlineLabel(Label):
    pass


class DatabaseScreenManager(ScreenManager):
    file = StringProperty(None)
    context = ObjectProperty(None)
    notes = NumericProperty(5)
    current_window = NumericProperty(0)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(DispScreen(name="home"))
        self.context = context.Context()


    def load(self, path, filename):
        index = 0
        self.file = os.path.join(path, filename[0])
        self.context = context.Context(self.file)
        self.get_screen(self.current).dismiss_popup()
        for widget in self.children:
            self.remove_widget(widget)
        self.add_widget(DispScreen(name=f'screen{index}'))
        row = 1
        for sportsman in self.context.content:
            self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.name))
            self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.cast))
            self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.position))
            self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.title))
            self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.sport))
            self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.rank))
            if row < self.notes:
                row += 1
            else:
                row = 1
                index += 1
                self.add_widget(DispScreen(name=f'screen{index}'))


    def save(self, path, filename):
        self.context.save_context(os.path.join(path, filename))
        self.get_screen(self.current).dismiss_popup()


    def next(self):
        if self.current_window < floor(len(self.context.content)/self.notes):
            self.current = 'screen{}'.format(self.current_window+1)
            self.current_window += 1

    def last(self):
        self.current_window = floor(len(self.context.content)/self.notes)
        self.current = f'screen{floor(len(self.context.content)/self.notes)}'


    def prev(self):
        if self.current_window > 0:
            self.current = 'screen{}'.format(self.current_window-1)
            self.current_window -= 1


    def first(self):
        self.current_window = 0
        self.current = 'screen0'
    pass


class DispScreen(Screen):
    table = ObjectProperty(None)

    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.table = TableOutline(pos_hint={'x': 0, 'top': 1})
        self.add_widget(self.table)


    def dismiss_popup(self):
        self._popup.dismiss()


    def show_load(self):
        content = dialogs.DialogLoader(load=self.parent.load, cancel=self.dismiss_popup)
        self._popup = dialogs.DialogPopup(title='Load file', content=content)
        self._popup.open()


    def show_save(self):
        content = dialogs.DialogSaver(save=self.parent.save, cancel=self.dismiss_popup)
        self._popup = dialogs.DialogPopup(title='Save file', content=content)
        self._popup.open()


    def show_add(self):
        content = dialogs.AddNoteDialog(add=self.add, cancel=self.dismiss_popup)
        self._popup = dialogs.DialogPopup(title='Add note', content=content)
        self._popup.open()


    def show_delete(self):
        content = dialogs.DeleteNoteDialog(delete=self.delete, cancel=self.dismiss_popup)
        self._popup = dialogs.DialogPopup(title='Delete note', content=content)
        self._popup.open()


    def add(self, name: str, cast: str, position: str, title: str, sport: str, rank: str):
        self.parent.context.add_to_context(name, cast, position, title, sport, rank)
        self.table.add_widget(TableOutlineLabel(text=name))
        self.table.add_widget(TableOutlineLabel(text=cast))
        self.table.add_widget(TableOutlineLabel(text=position))
        self.table.add_widget(TableOutlineLabel(text=title))
        self.table.add_widget(TableOutlineLabel(text=sport))
        self.table.add_widget(TableOutlineLabel(text=rank))
        self.dismiss_popup()


    def delete(self, tag_name: str, info: str):
        deleted = self.parent.context.delete_from_context(tag_name, info)
        for widget in self.children:
            if isinstance(widget, TableOutline):
                self.remove_widget(widget)
        self.table = TableOutline()
        self.add_widget(self.table)
        for i in self.parent.context.content:
            self.table.add_widget(TableOutlineLabel(text=i.name))
            self.table.add_widget(TableOutlineLabel(text=i.cast))
            self.table.add_widget(TableOutlineLabel(text=i.position))
            self.table.add_widget(TableOutlineLabel(text=i.title))
            self.table.add_widget(TableOutlineLabel(text=i.sport))
            self.table.add_widget(TableOutlineLabel(text=i.rank))
        self.dismiss_popup()

        content = dialogs.ResultDialog(result=deleted, close=self.dismiss_popup)
        self._popup = dialogs.ResultPopup(title='', content=content)
        self._popup.open()
    pass


class DatabaseApp(App):
    def build(self):
        return DatabaseScreenManager()


Builder.load_file('./ui/sport.kv')
