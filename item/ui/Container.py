from item.display.ImageLoader import ImageLoader
from item.ui.UI import UI
import pygame as p

class Container(UI):
    def __init__(self, rect : p.Rect):
        super().__init__()

        self.original_rect = rect

        self.change_order_layer(100)
        self.block_raycast = False

        self.on_resize_window += self.__on_resize_window
    
    def __on_resize_window(self):
        if self.original_rect is not None:
            self.rect = ImageLoader.resize_rect(self.original_rect)