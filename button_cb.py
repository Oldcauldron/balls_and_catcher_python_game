
import pygame
import pygame.font


class Button():
    def __init__(self, screen, st, stat, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (52, 154, 203)
        self.text_color = (52, 0, 0)

        self.font = pygame.font.SysFont('arial', 35)

        self.image = pygame.image.load('images/button.gif')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        """
        rect в данном случае похоже на специальный маленький
        экранчик для кнопки, который будет реагировать например на
        коллизию с мышкой. Похоже текст.рендер на это не способен
        """
        # self.rect = pygame.Rect(0, 0, self.width, self.height)
        # self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """
        render текста - рисует текст на новой Surface.
        Похоже это просто картинка как фон и не распознается как объект(?)
        Атрибуты - сам текст, сглаживание, цвет текста, background
        """
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, stat):
        """куда заливаем и где бликуем) На screen'е конечно"""
        # 1. на экране цвет кнопки заливаем в заданный прямоугольник
        # 2. на экране бликуем рендер шрифта в его прямоугольнике
        # self.screen.fill(self.button_color, self.rect)
        if not stat.game_active:
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)


