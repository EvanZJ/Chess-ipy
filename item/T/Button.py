import pygame as p
from item.T.GameObject import GameObject

class Button(GameObject):
    def __init__(self, x, y, sprite: p.Surface, scale):
        super().__init__()
        self.x = x
        self.y = y
        self.sprite = sprite
        self.sprite = p.transform.scale(self.sprite, (int(self.sprite.get_width() * scale), int(self.sprite.get_height() * scale)))
        
        self.on_awake += self.__awake
        self.on_draw += self.__draw

    def __awake(self):
        self.rect.topleft = (self.x, self.y)

    def __draw(self):
        self.screen.blit(self.sprite, self.rect)