import pygame as p
from item.core.GameObject import GameObject
from item.ui.InputField import InputField
from item.ui.Text import Text
from item.ui.TextButton import TextButton
from item.ui.button.CloseButton import CloseButton

class CreateRoom(GameObject):
    def __init__(self, width: int = 500, height: int = 600, color : p.Color = p.Color("white"), border : int = 16):
        super().__init__()
        
        self.width = width
        self.height = height
        self.color = color
        self.border = border

        self.on_awake += self.__awake
        self.on_draw += self.__draw

    def __awake(self):
        self.rect = p.Rect(
            (self.screen.get_width() - self.width) // 2,
            (self.screen.get_height() - self.height) // 2,
            self.width,
            self.height
        )
        self.title = self.instantiate(Text("Create Room", 48), self)
        self.title.anchor(self.rect, (0.5, 0), (0.5, 0))
        self.title.set_margin(top = 60)

        self.name_input = self.__create_input_field("Name", 160)
        self.create_button = self.__create_button("Create", 50)
        
        self.__create_close_button()

    def __draw(self):
        self.screen.fill((0, 0, 0))
        p.draw.rect(self.screen, self.color, self.rect, 0, self.border)

    def __create_input_field(self, text : str, top_margin : int) -> TextButton:
        input_field = self.instantiate(InputField(
            p.Rect(0, 0, 400, 50),
            p.Color(255, 255, 255, 50),
            placeholder = text, 
            placeholder_size = 24
        ), self)
        input_field.anchor(self.rect, (0.5, 0), (0.5, 0))
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
        button.anchor(self.rect, (0.5, 1), (0.5, 1))
        button.set_margin(bottom = bottom_margin)
        return button
    
    def __create_close_button(self):
        self.close_button = self.instantiate(CloseButton(48), self)
        self.close_button.anchor(self.rect, (1, 0), (1, 0))
        self.close_button.set_margin(top = 20, right = 20)
        self.close_button.on_mouse_down += self.destroy