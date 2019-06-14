
import random


class Settings():
    def __init__(self):

        self.screen_w = 1300
        self.screen_h = 650

        self.speed_factor = 3

        # громкость эффектов
        self.effects_volume = 0.3

        # pause activator
        self.pause = True

        # ожидание перед появлением зайцев
        self.waiting_time_for_balls = False

        # для разового пропуска мимо bullet update
        self.lost_bullet_update = False

        # со скольки зайцев делать start position герою
        self.balls_on_screen_for_startposition = 3

        self.initial_dinamic_set()
        self.reset_lost_balls_level()

    def initial_dinamic_set(self):
        # через сколько сбежавших зайцев проигрываешь
        self.limit_heroes = 3
        self.num_balls_on_screen = 2
        self.quicker_balls = 3 + self.num_balls_on_screen
        self.catcher_speed_moving = 11

    def reset_lost_balls_level(self):
        """сбрасываем счетчик лимита сбежавших зайцев"""
        self.lost_balls_level = 6

    def rand(self):
        """
        рандомное число, используем для задания скорости balls
        self.num_balls_on_screen подсчитывает количество зайцев
        на экране, причем происходит прирост благодаря коллизиям
        это число используем и для увеличения скорости с увеличением
        количества balls на экране
        """
        self.num = round(random.randrange(
            -self.quicker_balls, self.quicker_balls) + random.random(), 1)
        return self.num



#