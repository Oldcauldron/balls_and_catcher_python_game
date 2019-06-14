

class GameStat():
    def __init__(self, st):
        self.st = st
        # self.escape_level = self.st.lost_balls_level
        # self.limit_heroes = self.st.limit_heroes
        # self.reset_stat()
        self.game_active = False

        self.high_score = 0

        self.reset_stat()
        # self.num_balls_on_screen = self.st.num_balls_on_screen
        # self.quicker_balls = self.num_balls_on_screen + self.st.quicker_balls

    def reset_stat(self):
        # сколько коллизий
        self.collis = 0
        # сколько сбежало
        self.escaped_score = 0
        # уровень
        self.level = 1


