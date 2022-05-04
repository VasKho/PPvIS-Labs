import pygame
import yaml
import pygame_menu


class Menu:
    def __init__(self, display, **kwargs) -> None:
        self.display = display
        self.theme = pygame_menu.Theme()
        with open("menu/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            self.theme.background_color = pygame.Color(conf['back_color'])
            self.theme.widget_font = conf['font_path']
            self.theme.widget_font_color = conf['font_color']
            self.theme.widget_border_color = conf['button_color']
            self.theme.title_font_size = conf['name_font_size']
            self.theme.widget_font_size = conf['buttons_font_size']
            self.theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

        self.menu = pygame_menu.Menu('', 
                pygame.display.Info().current_w,
                pygame.display.Info().current_h,
                theme=self.theme
                )
        self.menu.add.vertical_fill()
        self.menu.add.label("PREVENTIVE STRIKE", font_size=self.theme.title_font_size)
        self.menu.add.vertical_fill()
        self.menu.add.button('Play', kwargs['start'])
        self.menu.add.vertical_fill()
        self.menu.add.button('Score', kwargs['show_score'])
        self.menu.add.vertical_fill()
        self.menu.add.button('Help', kwargs['help'])
        self.menu.add.vertical_fill()
        self.menu.add.button('Exit', pygame_menu.events.EXIT)
        self.menu.add.vertical_margin(300)


    def run(self):
        self.menu.mainloop(self.display)
