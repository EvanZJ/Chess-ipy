import pygame as p
from item.core.GameObject import GameObject
from item.display.ImageLoader import ImageLoader

class LegalMoveCircle(GameObject):
    def __init__(self, rect : p.Rect):
        super().__init__()

        self.rect = rect
        self.block_raycast = False

        self.on_draw += self.__draw

    def __draw(self):
        # p.draw.circle(self.screen, p.Color("red"), self.rect.center, 10)
        ImageLoader.draw_circle(p.Color("red"), self.rect, 10)
