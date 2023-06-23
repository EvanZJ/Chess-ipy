import pygame as p
from item.core.Event import Event
from item.core.GameObject import GameObject
from item.display.ImageLoader import ImageLoader
from item.ui.InputField import InputField
from item.ui.Text import Text
from item.ui.TextButton import TextButton
from item.ui.button.CloseButton import CloseButton

class JoinRoom(GameObject):
    def __init__(self, width: int = 500, height: int = 600, color : p.Color = p.Color("white"), border : int = 16):
        super().__init__()

        self.inputs : list[InputField] = []
        
        self.width = width
        self.height = height
        self.color = color
        self.border = border
        self.original_rect = None

        self.on_resize_window += self.__on_resize_window
        self.on_awake += self.__awake
        self.on_draw += self.__draw

    def __on_resize_window(self):
        if self.original_rect is not None:
            self.rect = ImageLoader.resize_rect(self.original_rect)

    def __awake(self):
        self.original_rect = p.Rect(
            0,
            0,
            self.width,
            self.height
        )
        self.original_rect.center = ImageLoader.get_instance().reference_rect.center
        self.rect = ImageLoader.resize_rect(self.original_rect)
        self.title = self.instantiate(Text("Join Room", 48), self)
        self.title.set_anchor((0.5, 0))
        self.title.set_pivot((0.5, 0))
        self.title.set_margin(top = 60)

        room_input = self.__create_input_field("Room", 140)
        self.inputs.append(room_input)
        name_input = self.__create_input_field("Name", 200)
        self.inputs.append(name_input)

        for input_field in self.inputs:
            input_field.on_focus += self.on_focus_input

        self.__create_button("Join", 50).on_mouse_down += lambda event : self.load_scene(2, name_input.user_input, True, room_input.user_input)
        
        self.__create_close_button()

    def __draw(self):
        self.screen.fill((0, 0, 0))
        p.draw.rect(self.screen, self.color, self.rect, 0, self.border)

    def __create_input_field(self, text : str, top_margin : int) -> InputField:
        input_field = self.instantiate(InputField(
            p.Rect(0, 0, 400, 50),
            p.Color(255, 255, 255, 50),
            placeholder = text, 
            placeholder_size = 24
        ), self)
        input_field.set_anchor((0.5, 0))
        input_field.set_pivot((0.5, 0))
        input_field.set_margin(top = top_margin)
        return input_field
    
    def __create_button(self, text : str, bottom_margin : int) -> TextButton:
        button = self.instantiate(TextButton(
            p.Rect(0, 0, 220, 60),
            p.Color(255, 255, 255, 50),
            8,
            text = text, 
            text_size = 36
        ), self)
        button.set_anchor((0.5, 1))
        button.set_pivot((0.5, 1))
        button.set_margin(bottom = bottom_margin)
        return button
    
    def __create_close_button(self):
        self.close_button = self.instantiate(CloseButton(48), self)
        self.close_button.set_anchor((1, 0))
        self.close_button.set_pivot((1, 0))
        self.close_button.set_margin(top = 20, right = 20)
        self.close_button.on_mouse_down += lambda event : self.destroy()

    def on_focus_input(self, focused_input_field : InputField):
        for input_field in self.inputs:
            if input_field == focused_input_field:
                continue
            input_field.set_focus(False)