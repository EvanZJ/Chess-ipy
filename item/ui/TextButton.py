import pygame as p
from item.ui.Text import Text
from item.ui.UI import UI

class TextButton(UI):
    def __init__(self, rect : p.Rect = None, color : p.Color = p.Color("green"), border : int = 0, text : str = "", text_size : int = 18):
        super().__init__()
        self.text : Text = None
        self.text_str = text
        self.text_size = text_size
        self.color = color
        self.border = border
        if isinstance(rect, p.Rect):
            self.sprite = p.Surface((rect.width, rect.height), p.SRCALPHA)
            self.sprite.fill(color, rect)

        self.on_awake += self.__awake
        self.on_enable += self.__on_enable
        self.on_disable += self.__on_disable

    def __awake(self):
        if self.text_str and isinstance(self.rect, p.Rect):
            self.text = self.instantiate(Text(self.text_str, self.text_size), self)
            self.text.set_anchor((0.5, 0.5))
            self.text.set_pivot((0.5, 0.5))

    def __on_enable(self):
        self.text.set_active(True)

    def __on_disable(self):
        self.text.set_active(False)