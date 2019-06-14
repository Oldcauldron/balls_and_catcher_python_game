
import pygame
from pygame.sprite import Sprite


class Catcher(Sprite):
    def __init__(self, st, screen, stat):
        super().__init__()
        self.st = st
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stat = stat

        image = self.number_hero_image()

        # if st.limit_heroes == 3:
        #     image = 'images/i.gif'
        # elif st.limit_heroes == 2:
        #     image = 'images/i2.gif'
        # elif st.limit_heroes <= 1:
        #     image = 'images/i3.gif'

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.y = (self.screen_rect.bottom - (self.rect.height))
        self.rect.x = (self.screen_rect.centerx - (self.rect.width / 2))

        # print('self.rect.bottom = {}'.format(self.rect.bottom))
        # print('self.screen_rect.bottom = {}'.format(self.screen_rect.bottom))
        # print('self.rect.centerx = {}'.format(self.rect.centerx))
        # print('screen_rect.centerx = {}'.format(self.screen_rect.centerx))

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        # if (self.rect.x > 0 and
        #         self.rect.x < (self.st.screen_w + self.rect.width)):
        self.speed = self.st.catcher_speed_moving + self.st.num_balls_on_screen
        if (self.moving_right and
                self.rect.x < (self.st.screen_w - self.rect.width)):
            self.x += self.speed
        if self.moving_left and self.rect.x >= 0:
            self.x -= self.speed
        # if (self.rect.y > 0 and
        #         self.rect.y < (self.st.screen_h + self.rect.height)):
        if self.moving_up and self.rect.y > 0:
            self.y -= self.speed
        if (self.moving_down and
                self.rect.y < (self.st.screen_h - self.rect.height)):
            self.y += self.speed
        self.rect.x = self.x
        self.rect.y = self.y
        # print(self.speed)

        # print('self.rect.x - {}'.format(self.rect.x))
        # print('self.rect.y - {}'.format(self.rect.y))

    def blit_me(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def start_position(self):
        self.y = (self.screen_rect.bottom - (self.rect.height))
        self.x = (self.screen_rect.centerx - (self.rect.width / 2))
        self.rect.x = self.x
        self.rect.y = self.y
        # self.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.update()
        self.blit_me()

    def number_hero_image(self):
        if self.st.limit_heroes == 3:
            return 'images/i.gif'
        elif self.st.limit_heroes == 2:
            return 'images/i2.gif'
        elif self.st.limit_heroes <= 1:
            return 'images/i3.gif'



        
        # print('self.rect.x - {}'.format(self.rect.x))
        # print('self.rect.y - {}'.format(self.rect.y))









#