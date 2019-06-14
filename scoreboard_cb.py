
import pygame
import pygame.font
from pygame.sprite import Group

from catcher_cb import Catcher


class Scoreboard():
    def __init__(self, st, stat, screen):
        self.st = st
        self.stat = stat
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont('arial', 35)
        self.text_color = (255, 255, 255)

        self.prep_images()

    def prep_images(self):
        self.prep_high_score()
        self.prep_escaped_score()
        self.prep_catch_score()
        self.prep_level_score()
        self.prep_limit_hero()
        self.prep_pause()

    def prep_high_score(self):
        high_score_str = str('High score - {}'.format(self.stat.high_score))
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 10
        self.high_score_rect.top = self.screen_rect.top + 10

    def prep_escaped_score(self):
        escaped_str = str('Escaped - {}'.format(self.stat.escaped_score))
        self.escaped_image = self.font.render(
            escaped_str, True, self.text_color)
        self.escaped_rect = self.escaped_image.get_rect()
        self.escaped_rect.left = self.screen_rect.left + 10
        self.escaped_rect.top = self.high_score_rect.bottom + 10

    def prep_catch_score(self):
        """пойманные"""
        catch_str = str('You catch - {}'.format(self.stat.collis))
        self.catch_image = self.font.render(catch_str, True, self.text_color)
        self.catch_rect = self.catch_image.get_rect()
        self.catch_rect.left = self.screen_rect.left
        self.catch_rect.top = self.escaped_rect.bottom + 10

    def prep_level_score(self):
        level_str = str('Level - {}'.format(self.stat.level))
        self.level_image = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = self.screen_rect.top + 10

    def prep_limit_hero(self):
        # limit_hero_str = str(
            # 'Limit heroes - {}'.format(self.st.limit_heroes))
        # self.limit_hero_image = self.font.render(
        #     limit_hero_str, True, self.text_color)
        # self.limit_hero_rect = self.limit_hero_image.get_rect()
        # self.limit_hero_rect.right = self.screen_rect.right - 10
        # self.limit_hero_rect.top = self.high_score_rect.bottom + 10
        self.catchers_group_scoreboard = Group()

        for catchers in range(self.st.limit_heroes):
            self.catcher_scoreboard = Catcher(self.st, self.screen, self.stat)
            self.catcher_scoreboard.image = pygame.transform.scale(
                self.catcher_scoreboard.image, (70, 70))
            self.catcher_scoreboard.rect =\
                self.catcher_scoreboard.image.get_rect()
            self.catcher_scoreboard.rect.top = self.screen_rect.top + 10
            self.catcher_scoreboard.rect.x = (
                self.screen_rect.right - (
                    self.catcher_scoreboard.rect.width * catchers) - 70)
            self.catchers_group_scoreboard.add(self.catcher_scoreboard)


    def prep_pause(self):
        self.pause_image = self.font.render('PAUSE', True, self.text_color)
        self.pause_rect = self.pause_image.get_rect()
        self.pause_rect.centerx = self.screen_rect.centerx
        self.pause_rect.centery = self.screen_rect.centery

    def draw_score(self):
        self.screen.blit(self.escaped_image, self.escaped_rect)
        self.screen.blit(self.catch_image, self.catch_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # self.screen.blit(self.limit_hero_image, self.limit_hero_rect)
        self.catchers_group_scoreboard.draw(self.screen)
        if not self.st.pause:
            self.screen.blit(self.pause_image, self.pause_rect)

