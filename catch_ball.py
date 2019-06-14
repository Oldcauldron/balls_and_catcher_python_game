
import pygame
from pygame.sprite import Group
from time import sleep

from settings_cb import Settings
from catcher_cb import Catcher
import func_cb as func
from statist_cb import GameStat
from button_cb import Button
from scoreboard_cb import Scoreboard


def run_game():

    pygame.init()
    pygame.display.set_caption('catcher and balls')

    st = Settings()
    stat = GameStat(st)

    screen = pygame.display.set_mode((st.screen_w, st.screen_h))
    screen_rect = screen.get_rect()
    bg = pygame.image.load('images/bg.jpg')
    bg = pygame.transform.scale(bg, (st.screen_w, st.screen_h))
    bg_rect = bg.get_rect()
    bg_rect.center = screen_rect.center

    sb = Scoreboard(st, stat, screen)

    catcher_z = Group()
    balls = Group()
    # catcher = Catcher(screen_rect, st, screen, stat)
    # catcher_z.add(catcher)
    play_button = Button(screen, st, stat, 'Play')

    # collis = 0

    # pygame.mixer.music.load('sound/start.ogg')
    # pygame.mixer.music.play()

    while True:

        """
        первого героя создает и потом если получил catcher_z.empty() от
        func.leveling
        """
        if len(catcher_z) == 0:
            catcher = Catcher(st, screen, stat)
            catcher_z.add(catcher)

        screen.blit(bg, (0, 0))
        # sb.draw_score()

        # рисует кнопку если game_active = False
        play_button.draw_button(stat)

        func.check_events(catcher, st, stat, balls, catcher_z, play_button)

        """
        слежение за коллизией(герой-зайцы)
        удаление зайцев
        подсчет ушедших и пойманных
        добавление нового зайца по уровню
        обновление счетов
        """
        func.collision_and_removing_balls(
            balls, screen_rect, st, func, catcher_z, stat, screen, sb)

        """
        если лимит сбежавших зайцев == 0 а game active = True:
            уменьшает лимит героев, создает нового героя, обновляет лимитзайцев
            и управляет game active
            если лимит героев закончился то game active False
        """
        func.leveling(
            balls, screen_rect, st, func, catcher_z, stat, screen)

        # screen.blit(bg, (0, 0))

        """
        если ушедших меньше лимита допускающего это включаем добавление
        Добавляет зайцев если len(balls)==0
        """
        if stat.game_active and st.pause:
            if len(balls) == 0:
                func.adding_balls(balls, st, screen_rect, func, catcher, stat)
                # там - catcher.start_position()
                st.lost_bullet_update = False
                # catcher.update()
                # catcher.blit_me()
            else:
                catcher.update()
                catcher.blit_me()
                balls.update()
                balls.draw(screen)
                st.lost_bullet_update = True

        pygame.display.flip()

        # чтобы зайцы появлялись после hero с небольшой задержкой
        if st.lost_bullet_update is False:
            sleep(0.9)


run_game()






#