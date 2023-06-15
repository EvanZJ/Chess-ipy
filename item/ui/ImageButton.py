import pygame as p
from item.ui.Text import Text
from item.ui.UI import UI

class ImageButton(UI):
    def __init__(self, x : float = 0, y : float = 0, sprite: p.Surface = None, scale : float = 0, text : str = "", text_size : int = 18):
        super().__init__()
        self.x = x
        self.y = y
        self.text = text
        self.text_size = text_size
        self.sprite = sprite
        self.scale_xy = scale

        self.on_awake += self.__awake

    def __awake(self):
        self.move(self.x, self.y)
        self.scale(int(self.sprite.get_width() * self.scale_xy), int(self.sprite.get_height() * self.scale_xy))