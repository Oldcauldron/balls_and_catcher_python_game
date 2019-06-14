
import pygame
import sys
# from time import sleep

from ball_cb import Ball
# from catcher_cb import Catcher


def check_events(catcher, st, stat, balls, catcher_z, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # print('escapted - {}'.format(stat.escaped_score))
            # print('you catch - {}'.format(stat.collis))
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, catcher, catcher_z, balls, stat, st)
        elif event.type == pygame.KEYUP and stat.game_active:
            check_keyup(event, catcher)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(
                mouse_x, mouse_y, catcher_z, balls, stat, play_button, st)


def check_keydown(event, catcher, catcher_z, balls, stat, st):
    if stat.game_active:
        if event.key == pygame.K_RIGHT:
            catcher.moving_right = True
        if event.key == pygame.K_LEFT:
            catcher.moving_left = True
        if event.key == pygame.K_UP:
            catcher.moving_up = True
        if event.key == pygame.K_DOWN:
            catcher.moving_down = True

    if event.key == pygame.K_q:
        # print('escapted - {}'.format(stat.escaped_score))
        # print('you catch - {}'.format(stat.collis))
        sys.exit()
    elif event.key == pygame.K_KP_ENTER or\
        event.key == pygame.K_SPACE or\
            event.key == pygame.K_RETURN:
                start_game(catcher_z, balls, stat, st)
    if event.key == pygame.K_ESCAPE:
        if st.pause:
            st.pause = False
        elif not st.pause:
            st.pause = True


def check_keyup(event, catcher):
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = False
    if event.key == pygame.K_LEFT:
        catcher.moving_left = False
    if event.key == pygame.K_UP:
        catcher.moving_up = False
    if event.key == pygame.K_DOWN:
        catcher.moving_down = False


def check_play_button(
        mouse_x, mouse_y, catcher_z, balls, stat, play_button, st):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(catcher_z, balls, stat, st)


def start_game(catcher_z, balls, stat, st):
    if not stat.game_active:
        pygame.mixer.music.load('sound/start.ogg')
        pygame.mixer.music.play()
        catcher_z.empty()
        balls.empty()
        stat.reset_stat()
        st.initial_dinamic_set()
        st.reset_lost_balls_level()
        pygame.mouse.set_visible(False)
        stat.game_active = True


def collision_and_removing_balls(
        balls, screen_rect, st, func, catcher_z, stat, screen, sb):
    # print('before collision len balls ', len(balls))
    collisions = pygame.sprite.groupcollide(balls, catcher_z, True, False)
    # sound_collis = pygame.mixer.Sound('sound/collis3.mp3')
    sound_esc = pygame.mixer.Sound('sound/esc.ogg')
    sound_esc.set_volume(st.effects_volume)

    if collisions:
        # sound_collis.play()
        for catcher_z in collisions.values():
            stat.collis += len(catcher_z)
        if (stat.collis % 25 == 0):
            st.num_balls_on_screen += 1
            stat.level += 1
        if stat.collis > stat.high_score:
            stat.high_score = stat.collis

    # считаем сбежавших и удаляем их
    for ball in balls:
        if ball.rect.x < -60 or\
                ball.rect.x > (st.screen_w + 50) or\
                ball.rect.y < -60 or\
                ball.rect.y > (st.screen_h + 50):
            sound_esc.play()
            balls.remove(ball)
            # оставшихся уровней на 1 меньше
            st.lost_balls_level -= 1
            # Сбежавших на 1 больше
            stat.escaped_score += 1
    sb.prep_images()  # изображаем все score
    sb.draw_score()


def leveling(balls, screen_rect, st, func, catcher_z, stat, screen):
    if st.lost_balls_level == 0 and stat.game_active:
        catcher_z.empty()
        st.limit_heroes -= 1

        if st.limit_heroes > 0:
            # если лимит героев не закончен обновляем сбежавших зайцев
            st.reset_lost_balls_level()
        elif st.limit_heroes <= 0:
            # print('escapted - {}'.format(stat.escaped_score))
            # print('you catch - {}'.format(stat.collis))
            stat.game_active = False
            pygame.mouse.set_visible(True)


def adding_balls(balls, st, screen_rect, func, catcher, stat):
    # if len(balls) == 0:
    for i in range(st.num_balls_on_screen):
        # print('num_balls_on_screen - {}'.format(st.num_balls_on_screen))
        ball = Ball(screen_rect, st, func, stat)
        balls.add(ball)
    if st.num_balls_on_screen >= st.balls_on_screen_for_startposition:
        catcher.start_position()
    else:
        catcher.update()
        catcher.blit_me()







#