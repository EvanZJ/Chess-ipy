import pygame as p
from item.ui.UI import UI

class Text(UI):
    def __init__(self, text : str, size : int = 18, color : p.Color = p.Color("white"), font : p.font.Font = None):
        super().__init__()

        self.size = size
        self.color = color
        self.font = font
        self.sprite = p.font.Font(font, size).render(text, True, color)
        self.block_raycast = False

    def change_text(self, text: str):
        self.sprite = p.font.Font(self.font, self.size).render(text, True, self.color)
        x = self.rect.x
        y = self.rect.y
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y

