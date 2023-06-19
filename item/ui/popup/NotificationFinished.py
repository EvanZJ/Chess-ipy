import pygame as p
from item.core.GameObject import GameObject
from item.ui.ImageButton import ImageButton
from item.ui.TextRender import TextRender
from item.ui.button.RetryButton import RetryButton

class NotificationFinished(GameObject):
    def __init__(self, x : int, y : int, scale : float, text : str):
        super().__init__()
        infoObject = p.display.Info()
        self.current_width = infoObject.current_w
        self.current_height = infoObject.current_h
        # print(self.current_width, self.current_height)
        self.order_layer = 4
        self.x = x
        self.y = y
        self.scale_xy = scale
        self.sprite : p.Surface = p.image.load("resource/images/notification.png")
        self.retry_button : RetryButton = None
        self.text = text
        self.render_text : TextRender = None
        # self.on_draw += self.__draw
        
        self.on_awake += self.__awake

    def __awake(self):
        self.rect = self.sprite.get_rect()
        self.scale(int(self.sprite.get_width() * self.scale_xy), int(self.sprite.get_height() * self.scale_xy))
        self.move(self.current_width/2 - self.rect.width/2, self.current_height/2 - self.rect.height/2)
        self.render_text = self.instantiate(TextRender(840,450,self.text, 50, p.Color("white")), self)
        self.text_rect = self.render_text.rect
        self.render_text.topleft = self.rect.topleft
        self.retry_button = self.instantiate(RetryButton(960,540,1.5), self)
        self.retry_button.set_anchor((0.5, 1))
        self.retry_button.set_pivot((0.5, 0.5))
        self.retry_button.set_margin(bottom = 100)

        
        # self.on_draw += self.__draw
