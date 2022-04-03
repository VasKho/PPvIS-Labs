from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner


class DialogPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(title_size=30, size_hint=(0.9, 0.9), **kwargs)
    pass


class ResultPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(title_size=30, size_hint=(0.5, 0.25), **kwargs)
    pass


class UpdatePopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(size_hint=(0.5, 0.2), **kwargs)
    pass


class UpdateRowsDialog(FloatLayout):
    change = ObjectProperty(None)
    pass


class ResultDialog(FloatLayout):
    result = NumericProperty(0)
    close = ObjectProperty(None)
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
    content = ObjectProperty(None)
    spinner = ObjectProperty(None)
    input = ObjectProperty(None)
    delete = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def modify_input(self):
        if self.spinner.text not in ['Состав', 'Разряд']:
            self.content.remove_widget(self.input)
            self.input = TextInput(multiline=False)
            self.content.add_widget(self.input)
        elif self.spinner.text == 'Состав':
            self.content.remove_widget(self.input)
            self.input = Spinner(text='N\\A', values=('Основной', 'Запасной', 'N\\A'))
            self.content.add_widget(self.input)
        elif self.spinner.text == 'Разряд':
            self.content.remove_widget(self.input)
            self.input = Spinner(text='Нет', values=('1-й юношеский', '2-й разряд', '3-й разряд', 'Кмс', 'Мастер спорта', 'Нет'))
            self.content.add_widget(self.input)
    pass
