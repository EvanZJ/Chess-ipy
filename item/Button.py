import pygame as p
from item.GameObject import GameObject

class Button(GameObject):
    def __init__(self, x : float, y : float, sprite: p.Surface, scale : float):
        super().__init__()
        self.x = x
        self.y = y
        self.sprite = sprite
        self.scale_xy = scale

        self.on_awake += self.__awake

    def __awake(self):
        self.move(self.x, self.y)
        self.scale(int(self.sprite.get_width() * self.scale_xy), int(self.sprite.get_height() * self.scale_xy))