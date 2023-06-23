from typing import cast
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
        self.min : int = 0
        self.max : int = 0
        self.scroll_position : int = 0
        self.scroll_delta : int = 30
        self.spacing : float = 20

        self.on_resize_window += self.__on_resize_window
        self.on_awake += self.__awake
        self.on_draw += self.__draw
        self.on_mouse_down += self.__on_mouse_down

    def __on_resize_window(self):
        if self.original_rect is not None:
            self.rect = ImageLoader.resize_rect(self.original_rect)
        self.recalculate_boundary()

    def __awake(self):
        container_rect = self.original_rect.copy()
        container_rect.width -= self.padding[0]
        container_rect.height -= self.padding[0]
        self.container = self.instantiate(Container(container_rect), self)
        self.container.set_anchor((0.5, 0.5))
        self.container.set_pivot((0.5, 0.5))

    def __draw(self):
        p.draw.rect(self.screen, self.color, self.rect, 0, self.border)

    def __on_mouse_down(self, event : p.event.Event):
        if event.button == p.BUTTON_WHEELUP:
            self.scroll(-self.scroll_delta)
        if event.button == p.BUTTON_WHEELDOWN:
            self.scroll(self.scroll_delta)

    def append(self, game_object : UI):
        top_margin = self.get_items_height()
        self.container.children.append(game_object)
        game_object.parent = self.container
        game_object.set_margin(top = top_margin)
        self.recalculate_boundary()

    def get_items_height(self):
        if self.container == None:
            return 0

        top_margin = 0
        for past_item in self.container.children:
            top_margin += past_item.sprite.get_rect().height + self.spacing
        return top_margin

    def scroll(self, delta : int):
        print(self.max)
        print(self.original_rect.height)
        print(self.scroll_position)
        if self.max < self.original_rect.height:
            return

        actual_delta = delta
        if self.scroll_position + delta < 0:
            actual_delta = -self.scroll_position

        if self.scroll_position + self.original_rect.height + delta > self.max:
            actual_delta = self.max - self.original_rect.height - self.scroll_position
        
        self.scroll_position += actual_delta
        for item in self.children:
            item_ui = cast(UI, item)
            item_ui.set_margin(bottom = item_ui.margin[2] + actual_delta)

    def recalculate_boundary(self):
        self.min = 0
        self.max = self.get_items_height()
        # temp_min : int = None
        # temp_max : int = None
        # for item in self.children:
        #     if item.rect == None:
        #         continue
            
        #     if temp_min == None:
        #         temp_min = item.rect.top
        #     elif item.rect.top < temp_min:
        #         temp_min = item.rect.top

        #     item_ui = cast(UI, item)
        #     if temp_max == None:
        #         temp_max = item.rect.bottom
        #     elif item.rect.bottom > temp_max:
        #         temp_max = item.rect.top
        
        # self.min = temp_min
        # self.max = temp_max