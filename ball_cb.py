
import pygame
from pygame.sprite import Sprite
import random


class Ball(Sprite):
    def __init__(self, screen_rect, st, func, stat):
        super().__init__()

        self.st = st
        self.screen_rect = screen_rect
        self.stat = stat
        self.func = func
        self.image = pygame.image.load('images/ball.gif')
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(150, (self.st.screen_w - 200))
        self.rect.y = random.randrange(150, (self.st.screen_h - 200))

        # self.rand = self.st.rand()
        # print('self.rect.x - {}, self.rect.y - {}'.
        # format(self.rect.x, self.rect.y))
        self.randx = self.st.rand()
        self.randy = self.st.rand()

    def update(self):
        self.rect.x += self.randx
        self.rect.y += self.randy
        # print('self.rect.x - {}, self.rect.y - {}'.format(
        # self.rect.x, self.rect.y))
        # print('self.rand.x ', self.randx)
        # print('self.rand.y ', self.randy)






    






#