from item.core.GameObject import GameObject
from item.display.ImageLoader import ImageLoader
from item.ui.Container import Container
from item.ui.UI import UI
import pygame as p

class ScrollView(UI):
    def __init__(self, rect : p.Rect, color : p.Color = p.Color("white"), border : int = 8, padding : tuple[float, float] = (0, 0)):
        super().__init__()
        self.original_rect = rect
        self.color = color
        self.border = border
        self.padding = padding
        self.container : Container = None

        self.on_resize_window += self.__on_resize_window
        self.on_awake += self.__awake
        self.on_draw += self.__draw

    def __on_resize_window(self):
        if self.original_rect is not None:
            self.rect = ImageLoader.resize_rect(self.original_rect)

    def __awake(self):
        container_rect = self.original_rect.copy()
        container_rect.width -= self.padding[0]
        container_rect.height -= self.padding[0]
        self.container = self.instantiate(Container(container_rect), self)
        self.container.set_anchor((0.5, 0.5))
        self.container.set_pivot((0.5, 0.5))

    def __draw(self):
        p.draw.rect(self.screen, self.color, self.rect, 0, self.border)

    def append(self, game_object : GameObject):
        game_object.parent = self.container