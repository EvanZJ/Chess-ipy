from item.core.Event import Event
from item.display.ImageLoader import ImageLoader
from item.ui.InputField import InputField
from item.ui.ScrollView import ScrollView
from item.ui.Text import Text
from item.ui.UI import UI
import pygame as p

class ChatUI(UI):
    def __init__(self, user : str, rect : p.Rect, color : p.Color = p.Color("white"), border : int = 8):
        super().__init__()
        self.user = user
        self.original_rect = rect
        self.color = color
        self.border = border
        self.messages_ori : list[tuple[str, str]] = []
        self.messages : list[Text] = []
        self.padding : tuple[float, float, float, float]

        self.on_resize_window += self.__on_resize_window
        self.on_awake += self.__awake
        self.on_draw += self.__draw

        self.on_user_message_enter = Event()

    def __on_resize_window(self):
        if self.original_rect is not None:
            self.rect = ImageLoader.resize_rect(self.original_rect)

    def __awake(self):
        self.__instantiate_scroll_view()
        self.__instantiate_input_field()

    def __draw(self):
        p.draw.rect(self.screen, self.color, self.rect, 0, self.border)

    def add_message(self, sender : str, message : str):
        self.messages_ori.append((sender, message))
        new_message = self.instantiate(Text(sender + ": " + message, 38, p.Color("black")))
        self.scroll_view.append(new_message)
        new_message.change_order_layer(52) 
        self.messages.append(new_message)

    def __instantiate_scroll_view(self):
        scroll_view_rect = self.original_rect.copy()
        scroll_view_rect.width -= 50
        scroll_view_rect.height -= 125
        self.scroll_view = self.instantiate(ScrollView(scroll_view_rect, p.Color(245, 210, 103), 0, (20, 20)), self)
        self.change_order_layer(50)
        self.scroll_view.change_order_layer(51)
        self.scroll_view.set_anchor((0.5, 0))
        self.scroll_view.set_pivot((0.5, 0))
        self.scroll_view.set_margin(top = 25)

    def __instantiate_input_field(self):
        self.input_field = self.instantiate(InputField(p.Rect(0, 0, self.scroll_view.original_rect.width, 38), placeholder = "Enter something...", placeholder_size = 32), self)
        self.input_field.set_anchor((0.5, 1))
        self.input_field.set_pivot((0.5, 1))
        self.input_field.set_margin(bottom = 25)
        self.input_field.change_order_layer(51)

        self.input_field.on_enter += self.__on_input_field_enter

    def __on_input_field_enter(self):
        message = self.input_field.user_input
        self.add_message(self.user, message)
        self.input_field.clear()
        self.on_user_message_enter(self.user, message)