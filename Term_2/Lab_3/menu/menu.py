import pygame
import yaml
import pygame_menu
from score_table.score import ScoreTable


class MenuTheme(pygame_menu.Theme):
    def __init__(self) -> None:
        super().__init__()
        with open("menu/config.yaml", 'r') as file:
            conf = yaml.safe_load(file)
            self.background_color = pygame.Color(conf['back_color'])
            self.widget_font = conf['font_path']
            self.widget_font_color = conf['font_color']
            self.widget_border_color = conf['button_color']
            self.title_font_size = conf['name_font_size']
            self.title_font = conf['font_path']
            self.title_font_color = conf['font_color']
            self.widget_font_size = conf['buttons_font_size']
            self.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE


class Menu:
    def __init__(self, display, start) -> None:
        self.display = display
        self.theme = MenuTheme()
        self.menu = pygame_menu.Menu('', 
                pygame.display.Info().current_w,
                pygame.display.Info().current_h,
                theme=self.theme
                )
        self.menu.add.vertical_fill()
        self.menu.add.label("PREVENTIVE STRIKE", font_size=self.theme.title_font_size)
        self.menu.add.vertical_fill()
        self.menu.add.button('Play', start)
        self.menu.add.vertical_fill()
        self.menu.add.button('Score', self._show_score)
        self.menu.add.vertical_fill()
        self.menu.add.button('Help', self._show_help)
        self.menu.add.vertical_fill()
        self.menu.add.button('Exit', pygame_menu.events.EXIT)
        self.menu.add.vertical_margin(300)


    def run(self):
        self.menu.mainloop(self.display)


    def _show_score(self):
        theme = MenuTheme()
        score_menu = pygame_menu.Menu('',
            pygame.display.Info().current_w,
            pygame.display.Info().current_h,
            theme=theme
            )
        button = score_menu.add.button("Back to menu", score_menu.disable)
        button.set_float(origin_position=True)
        table = score_menu.add.table()
        position = 1
        score_table = ScoreTable.read_from_xml("score_table/score_table.xml").fields
        for (key, value) in score_table.items():
            table.add_row([position, key, value], cell_align=pygame_menu.locals.ALIGN_LEFT, cell_padding=30)
            position += 1
        score_menu.mainloop(self.display)


    def _show_help(self):
        theme = MenuTheme()
        help_menu = pygame_menu.Menu('',
                pygame.display.Info().current_w,
                pygame.display.Info().current_h,
                theme=theme,
                center_content=False
                )
        help_menu.add.button("Back to menu", help_menu.disable)
        table = help_menu.add.table()
        table.add_row(["1, 2, 3", "Change weapon"], cell_align=pygame_menu.locals.ALIGN_LEFT, cell_padding=30)
        table.add_row(["w", "Move forward"], cell_align=pygame_menu.locals.ALIGN_LEFT, cell_padding=30)
        table.add_row(["s", "Move backward"], cell_align=pygame_menu.locals.ALIGN_LEFT, cell_padding=30)
        table.add_row(["a", "Move left"], cell_align=pygame_menu.locals.ALIGN_LEFT, cell_padding=30)
        table.add_row(["d", "Move right"], cell_align=pygame_menu.locals.ALIGN_LEFT, cell_padding=30)
        table.add_row(["Space", "Shoot"], cell_align=pygame_menu.locals.ALIGN_LEFT, cell_padding=30)
        table.add_row(["Up, Down, Left, Right arrows", "Rotate"], cell_align=pygame_menu.locals.ALIGN_LEFT, cell_padding=30)
        table.add_row(["ESC", "Exit game"], cell_align=pygame_menu.locals.ALIGN_LEFT, cell_padding=30)
        help_menu.mainloop(self.display)
