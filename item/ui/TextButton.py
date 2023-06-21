import pygame as p
from item.display.ImageLoader import ImageLoader
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
            self.set_sprite(self.__create_button_sprite(rect, color))
            print((rect.x, rect.y))
            self.set_coordinate((rect.x, rect.y))

        # self.on_resize_window += self.__on_resize_window
        self.on_awake += self.__awake
        self.on_enable += self.__on_enable
        self.on_disable += self.__on_disable

    # def __on_resize_window(self):
    #     if self.original_sprite is None:
    #         return
    #     self.sprite = ImageLoader.resize_surface(self.original_sprite)

    def __awake(self):
        print(self.coordinate)
        if self.text_str and isinstance(self.rect, p.Rect):
            self.text = self.instantiate(Text(self.text_str, self.text_size), self)
            self.text.set_anchor((0.5, 0.5))
            self.text.set_pivot((0.5, 0.5))

    def __on_enable(self):
        self.text.set_active(True)

    def __on_disable(self):
        self.text.set_active(False)

    def set_active(self, value : bool):
        self.enabled = value
        if(self.enabled == True):
            self.on_enable()
        else:
            self.on_disable()

    def __create_button_sprite(self, rect : p.Rect, color : p.Color) -> p.Surface :
        sprite = p.Surface((rect.width, rect.height), p.SRCALPHA)
        sprite.fill(color, rect)
        return sprite