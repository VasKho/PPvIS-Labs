import pygame
import score_table.score as st
from menu.menu import Menu
from level.level import Level, DEATH, PASS


def start_game():
    level_number = 1
    while level_number < max_levels:
        if level_number == 1:
            pygame.mixer.init()
            pygame.mixer.music.load('./soundtrack/game/doom.ogg')
            pygame.mixer.music.set_volume(0.7)
            level = Level(display, "level/config/level1.yaml")
            pygame.mixer.music.play()
            level.start()
            pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == DEATH:
                pygame.mixer.music.stop()
                return
            if event.type == PASS:
                level_number += 1
                level = Level(display, f"level/config/level{level_number}.yaml", event.score)
                pygame.mixer.music.unpause()
                level.start()
                pygame.mixer.music.pause()
    score_table = st.ScoreTable.read_from_xml("score_table/score_table.xml")
    name = level.map.get_input()
    if name:
        score_table.add(name=name, score=level.player.score)
    else: 
        score_table.add(name="Unknown", score=level.player.score)
    st.ScoreTable.write_to_xml(score_table, "score_table/score_table.xml")


pygame.init()
max_levels = 3
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
menu = Menu(display, start=start_game)
menu.run()
