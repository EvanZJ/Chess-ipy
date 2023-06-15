import pygame as p
from item.core.GameObject import GameObject

class UI(GameObject):
    def __init__(self):
        super().__init__()

        self.anchor : tuple[float, float] = (0, 0)
        self.pivot : tuple[float, float] = (0, 0)

        self.margin : tuple[float, float, float, float] = (0, 0, 0, 0)

        self.on_update += self.__on_update

    def __on_update(self):
        if isinstance(self.parent, GameObject):
            self.update_position(self.parent.rect)

    def update_position(self, rect : p.Rect):
        if isinstance(rect, p.Rect):
            self.rect.topleft = rect.topleft
            self.rect.x += rect.width * self.anchor[0]
            self.rect.y += rect.height * self.anchor[1]

            self.rect.x -= self.rect.width * self.pivot[0]
            self.rect.y -= self.rect.height * self.pivot[1]

            self.rect.y += self.margin[0]
            self.rect.x -= self.margin[1]
            self.rect.y -= self.margin[2]
            self.rect.x += self.margin[3]
            
    def set_anchor(self, anchored_to: tuple[float, float] = (0, 0)):
        self.anchor = anchored_to

    def set_pivot(self, pivot: tuple[float, float] = (0, 0)):
        self.pivot = pivot

    def set_margin(self, top: int = 0, right: int = 0, bottom: int = 0, left: int = 0):
        self.margin = (top, right, bottom, left)