import os

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
    max_rows = NumericProperty(5)
    max_windows = NumericProperty(1)
    current_window = NumericProperty(1)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(DispScreen(name='screen1'))
        self.context = context.Context()


    def load(self, path, filename):
        self.file = os.path.join(path, filename[0])
        self.context = context.Context(self.file)
        self.get_screen(self.current).dismiss_popup()
        self.out_context()


    def out_context(self):
        index = 1
        for widget in range(1, self.max_windows+1):
            self.remove_widget(self.get_screen(f'screen{widget}'))
        self.max_windows = 1
        self.add_widget(DispScreen(name=f'screen{index}', max_rows=self.max_rows, fields=len(self.context.content)))
        self.get_screen(f'screen{index}').rows = 1
        for sportsman in self.context.content:
            if self.get_screen(f'screen{index}').rows <= self.max_rows:
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.name))
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.cast))
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.position))
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.title))
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.sport))
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.rank))
            else:
                index += 1
                self.add_widget(DispScreen(name=f'screen{index}', max_rows=self.max_rows, fields=len(self.context.content)))
                self.max_windows += 1
                self.get_screen(f'screen{index}').rows = 1
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.name))
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.cast))
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.position))
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.title))
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.sport))
                self.get_screen(f'screen{index}').table.add_widget(TableOutlineLabel(text=sportsman.rank))
            self.get_screen(f'screen{index}').rows += 1


    def show_update(self):
        def set_new_max_rows(new_value):
            if new_value != '':
                self.max_rows = int(new_value)
            self.out_context()
            self._popup.dismiss()

        content = dialogs.UpdateRowsDialog(change=set_new_max_rows)
        self._popup = dialogs.UpdatePopup(title='', content=content)
        self._popup.open()


    def save(self, path, filename):
        self.context.save_context(os.path.join(path, filename))
        self.get_screen(self.current).dismiss_popup()


    def next(self):
        if self.current_window < self.max_windows:
            self.current = 'screen{}'.format(self.current_window+1)
            self.current_window += 1

    def last(self):
        self.current_window = self.max_windows
        self.current = f'screen{self.max_windows}'


    def prev(self):
        if self.current_window > 1:
            self.current = 'screen{}'.format(self.current_window-1)
            self.current_window -= 1


    def first(self):
        self.current_window = 1
        self.current = 'screen1'
    pass


class DispScreen(Screen):
    table = ObjectProperty(None)
    rows = NumericProperty(1)

    
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
        self.parent.out_context()
        self.dismiss_popup()


    def delete(self, tag_name: str, info: str):
        deleted = self.parent.context.delete_from_context(tag_name, info)
        self.parent.out_context()
        self.dismiss_popup()

        content = dialogs.ResultDialog(result=deleted, close=self.dismiss_popup)
        self._popup = dialogs.ResultPopup(title='', content=content)
        self._popup.open()
    pass


class DatabaseApp(App):
    def build(self):
        return DatabaseScreenManager()


Builder.load_file('./ui/sport.kv')
