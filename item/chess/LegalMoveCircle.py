import pygame as p
from item.core.GameObject import GameObject

class LegalMoveCircle(GameObject):
    def __init__(self, rect : p.Rect):
        super().__init__()

        self.rect = rect

        self.on_draw += self.__draw

    def __draw(self):
        p.draw.circle(self.screen, p.Color("red"), self.rect.center, 10)
