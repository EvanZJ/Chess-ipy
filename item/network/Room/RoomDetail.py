from item.core.GameObject import GameObject
import pygame as p
from item.display.ImageLoader import ImageLoader
from item.ui.Text import Text

class RoomDetail(GameObject):
    def __init__(self, rect : p.Rect, room_number : int, user_name : str):
        super().__init__()

        self.original_rect = rect
        self.rect = ImageLoader.resize_rect(self.original_rect)
        self.room_number = room_number
        self.user_name = user_name
        self.on_resize_window += self.__on_resize_window
        self.on_awake += self.__awake

    def __on_resize_window(self):
        self.rect = ImageLoader.resize_rect(self.original_rect)

    def __awake(self):
        self.room_number_text = self.instantiate(Text("Room number: " + str(self.room_number), 36), self)
        self.user_name_text = self.instantiate(Text("Username: " + str(self.user_name), 36), self)
        self.user_name_text.set_margin(top = 48)