import pygame


class Menu:
    BACK_COLOR = (0, 0, 0)
    FONT_COLOR = (255, 0, 0)
    BUTTON_COLOR = (255, 255, 255)
    def __init__(self, display: pygame.surface.Surface):
        self.size = display.get_size()
        self.display = display
        self.name_font = pygame.font.Font('./menu/src/PixelDevilsdeal.ttf', 60)
        self.button_font = pygame.font.Font('./menu/src/PixelDevilsdeal.ttf', 40)


    def run(self):
        running = True
        while running:
            self.display.fill(Menu.BACK_COLOR)

            name = self.name_font.render('HELL SLAYER', True, Menu.FONT_COLOR)
            self.display.blit(name, (self.size[0]/2-name.get_width()/2, self.size[1]//8))

            start = self.button_font.render('START', True, Menu.FONT_COLOR)
            self.display.blit(start, (self.size[0]//2-start.get_width()//2, self.size[1]//4))
            start_btn = pygame.draw.rect(self.display, Menu.BUTTON_COLOR, [self.size[0]//2-start.get_width()//2-10,
                                                                           self.size[1]//4-10,
                                                                           start.get_width()+20,
                                                                           start.get_height()+20],
                                                                           2)

            score = self.button_font.render('SCORE', True, Menu.FONT_COLOR)
            self.display.blit(score, (self.size[0]//2-start.get_width()//2, self.size[1]//2.7))
            score_btn = pygame.draw.rect(self.display, Menu.BUTTON_COLOR, [self.size[0]//2-start.get_width()//2-10,
                                                                           int(self.size[1]//2.7)-10,
                                                                           start.get_width()+20,
                                                                           start.get_height()+20],
                                                                           2)

            exit_button = self.button_font.render('EXIT', True, Menu.FONT_COLOR)
            self.display.blit(exit_button, (self.size[0]//2-start.get_width()//2, self.size[1]//2))
            exit_btn = pygame.draw.rect(self.display, Menu.BUTTON_COLOR, [self.size[0]//2-start.get_width()//2-10,
                                                                          self.size[1]//2-10,
                                                                          start.get_width()+20,
                                                                          start.get_height()+20],
                                                                          2)

            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if start_btn.collidepoint(mouse_pos):
                        running = False
                    if score_btn.collidepoint(mouse_pos):
                        pass
                    if exit_btn.collidepoint(mouse_pos):
                        exit()

            pygame.display.update()
