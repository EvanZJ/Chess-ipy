import json
import os
from item.core.Event import Event
from item.display.ImageLoader import ImageLoader
from item.ui.InputField import InputField
from item.ui.ScrollView import ScrollView
from item.ui.Text import Text
from item.ui.UI import UI
import pygame as p

class LoadMatchContainer(UI):
    def __init__(self, rect : p.Rect, color : p.Color = p.Color("white"), border : int = 8):
        super().__init__()
        self.user = "test"
        self.original_rect = rect
        self.color = color
        self.border = border
        self.messages_ori : list[tuple[str, str]] = []
        self.messages : list[Text] = []

        self.on_resize_window += self.__on_resize_window
        self.on_awake += self.__awake

        self.on_user_message_enter = Event()

    def __on_resize_window(self):
        if self.original_rect is not None:
            self.rect = ImageLoader.resize_rect(self.original_rect)

    def __awake(self):
        self.__instantiate_scroll_view()
        self.get_saved_match()

    def add_message(self, sender : str, message : str):
        self.messages_ori.append((sender, message))
        new_message = self.instantiate(Text(sender + ": " + message, 38, p.Color("black")))
        self.scroll_view.append(new_message)
        new_message.change_order_layer(52) 
        self.messages.append(new_message)

    def __instantiate_scroll_view(self):
        scroll_view_rect = self.original_rect.copy()
        self.scroll_view = self.instantiate(ScrollView(scroll_view_rect, p.Color(245, 210, 103), 0, (20, 20)), self)
        self.change_order_layer(50)
        self.scroll_view.change_order_layer(51)
        self.scroll_view.set_anchor((0.5, 0))
        self.scroll_view.set_pivot((0.5, 0))

    def get_saved_match(self):
        filenames = os.listdir("record")

        for filename in filenames:
            print(filename)
            saved_match = self.instantiate(Text(filename, 48, p.Color("black")))
            self.scroll_view.append(saved_match)
            saved_match.change_order_layer(52) 
            saved_match.block_raycast = True

            def on_mouse_down_handler(event, filename=filename):
                self.load_match(filename)

            saved_match.on_mouse_down += on_mouse_down_handler

    def load_match(self, filename):
        file_path = f'record/{filename}'

        with open(file_path, 'r') as file:
            json_data = json.load(file)

        print(json_data)
        self.load_scene(1, json.loads(json_data))