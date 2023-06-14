import pygame as p
from item.core.GameObject import GameObject
from item.ui.Button import Button
from item.ui.button.RetryButton import RetryButton

class NotificationFinished(GameObject):
    def __init__(self, x : int, y : int, scale : float):
        super().__init__()
        infoObject = p.display.Info()
        self.current_width = infoObject.current_w
        self.current_height = infoObject.current_h
        print(self.current_width, self.current_height)
        self.order_layer = 4
        self.x = x
        self.y = y
        self.scale_xy = scale
        self.sprite : p.Surface = p.image.load("resource/images/notification.png")
        self.instantiate(RetryButton(960,540,1))
        self.on_awake += self.__awake

    def __awake(self):
        self.scale(int(self.sprite.get_width() * self.scale_xy), int(self.sprite.get_height() * self.scale_xy))
        self.move(self.current_width/2 - self.rect.width/2, self.current_height/2 - self.rect.height/2)
        # self.on_draw += self.__draw
