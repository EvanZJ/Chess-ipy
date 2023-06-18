import pygame as p
from item.core.GameObject import GameObject

class TextRender(GameObject):
    def __init__(self, x : int, y :int, text : str, size : int = 8, color : p.Color = p.Color("white"), font : p.font.Font = None):
        super().__init__()
        self.size = size
        self.color = color
        self.font = font
        self.text = text
        self.x = x
        self.y = y
        self.sprite = p.font.Font(self.font, self.size).render(self.text, True, self.color)
        self.on_awake += self.__awake
        self.on_draw += self.__draw
    
    def __awake(self):
        # print('here')
        self.rect = self.sprite.get_rect()
        print(self.rect)
        self.change_order_layer(20)
        self.rect.topleft = (self.x, self.y)
        print(self.rect)
        print(self.sprite)
        self.set_active(True)

    def __draw(self):
        # print('here')
        print(self.text)
        self.screen.blit(self.sprite, self.rect)

    def set_active(self, value: bool):
        return super().set_active(value)