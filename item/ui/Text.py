import pygame as p
from item.ui.UI import UI

class Text(UI):
    def __init__(self, text : str, size : int = 8, color : p.Color = p.Color("white"), font : p.font.Font = None):
        super().__init__()

        self.size = size
        self.color = color
        self.font = font
        self.sprite = p.font.Font(font, size).render(text, True, color)
        self.block_raycast = False
        
    def change_text(self, text: str):
        self.sprite = p.font.Font(self.font, self.size).render(text, True, self.color)
        self.rect = self.sprite.get_rect()

    def set_active(self, value : bool):
        self.enabled = value
        if(self.enabled == True):
            self.on_enable()
        else:
            self.on_disable()