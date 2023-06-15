import pygame as p
from item.ui.TextButton import TextButton

class InputField(TextButton):
    def __init__(self, rect: p.Rect = None, color: p.Color = p.Color(255, 255, 255, 50), placeholder: str = "Input", placeholder_size : int = 18):
        super().__init__(rect, color, 0, placeholder, placeholder_size)

        self.user_input = ""
        self.focus = False
        self.on_mouse_down += lambda : self.set_focus(True)
        self.on_keyboard_down += self.__on_keyboard_down
        self.on_update += self.__update

    def __on_keyboard_down(self, event : p.key.ScancodeWrapper):
        if not self.focus:
            return

        if event.key == p.K_BACKSPACE:
            self.user_input = self.user_input[:-1]
        else:
            if event.unicode:
                self.user_input += event.unicode

    def __update(self):
        if self.focus:
            self.text.change_text(self.user_input)

    def set_focus(self, value : bool):
        self.focus = value