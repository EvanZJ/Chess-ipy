import pygame as p
from item.core.GameObject import GameObject

class UI(GameObject):
    def anchor(self, rect : p.Rect, anchored_to: tuple[float, float] = (0, 0), pivot: tuple[float, float] = [0, 0]):
        if isinstance(self.rect, p.Rect) and isinstance(rect, p.Rect):
            self.rect.topleft = rect.topleft
            self.rect.x += rect.width * anchored_to[0]
            self.rect.y += rect.height * anchored_to[1]

            self.rect.x -= self.rect.width * pivot[0]
            self.rect.y -= self.rect.height * pivot[1]

    def set_margin(self, top: int = 0, right: int = 0, bottom: int = 0, left: int = 0):
        if isinstance(self.rect, p.Rect):
            self.rect.y += top
            self.rect.x -= right
            self.rect.y -= bottom
            self.rect.x += left