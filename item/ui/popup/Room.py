import pygame as p
from item.core.GameObject import GameObject
from item.ui.Text import Text
from item.ui.TextButton import TextButton
from item.ui.button.CloseButton import CloseButton

class Room(GameObject):
    def __init__(self, width: int = 500, height: int = 600, color : p.Color = p.Color("white"), border : int = 16):
        super().__init__()
        
        self.width = width
        self.height = height
        self.color = color
        self.border = border

        self.on_awake += self.__awake
        self.on_draw += self.__draw
        self.on_enable += self.__on_enable
        self.on_disable += self.__on_disable

    def __awake(self):
        self.rect = p.Rect(
            (self.screen.get_width() - self.width) // 2,
            (self.screen.get_height() - self.height) // 2,
            self.width,
            self.height
        )
        self.title = self.instantiate(Text("Room", 48))
        self.title.anchor(self.rect, (0.5, 0), (0.5, 0))
        self.title.set_margin(top = 60)

        self.create_room_button = self.__create_button("Create Room", 200)
        self.join_room_button = self.__create_button("Join Room", 320)
        
        self.__create_close_button()

    def __draw(self):
        p.draw.rect(self.screen, self.color, self.rect, 0, self.border)

    def __on_enable(self):
        self.create_room_button.set_enable(True)
        self.title.set_enable(True)
        self.join_room_button.set_enable(True)
        self.close_button.set_enable(True)

    def __on_disable(self):
        self.create_room_button.set_enable(False)
        self.title.set_enable(False)
        self.join_room_button.set_enable(False)
        self.close_button.set_enable(False)

    def __create_button(self, text : str, top_margin : int) -> TextButton:
        button = self.instantiate(TextButton(
            p.Rect(0, 0, 280, 100),
            p.Color(255, 255, 255, 50),
            8,
            text = text, 
            text_size = 36
        ))
        button.anchor(self.rect, (0.5, 0), (0.5, 0))
        button.set_margin(top = top_margin)
        return button
    
    def __create_close_button(self):
        self.close_button = self.instantiate(CloseButton(48))
        self.close_button.anchor(self.rect, (1, 0), (1, 0))
        self.close_button.set_margin(top = 20, right = 20)
        self.close_button.on_mouse_down += lambda : self.set_enable(False)