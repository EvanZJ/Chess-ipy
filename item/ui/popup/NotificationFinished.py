import pygame as p
from item.core.GameObject import GameObject
from item.display.ImageLoader import ImageLoader
from item.ui.ImageButton import ImageButton
from item.ui.Text import Text
from item.ui.TextRender import TextRender
from item.ui.UI import UI
from item.ui.button.RetryButton import RetryButton

class NotificationFinished(UI):
    def __init__(self, x : int, y : int, scale : float, text : str):
        super().__init__()
        # infoObject = p.display.Info()
        # self.current_width = infoObject.current_w
        # self.current_height = infoObject.current_h
        self.reference_rect : p.Rect = ImageLoader.get_instance().reference_rect
        self.current_width = self.reference_rect.width
        self.current_height = self.reference_rect.height
        # print(self.current_width, self.current_height)
        self.order_layer = 4
        self.x = x
        self.y = y
        self.scale_factor = scale
        # self.sprite : p.Surface = p.image.load("resource/images/notification.png")
        self.sprite : p.Surface = ImageLoader.load("resource/images/notification.png")
        self.retry_button : RetryButton = None
        self.text = text
        # self.render_text : TextRender = None
        # self.on_draw += self.__draw
        
        self.on_awake += self.__awake

    def __awake(self):
        self.set_pivot((0.5, 0.5))
        # self.original_rect = self.sprite.get_rect()
        # self.set_coordinate((self.current_width/2 - self.original_rect.width, self.current_height/2 - self.original_rect.height))
        self.scale(int(self.sprite.get_width() * self.scale_factor), int(self.sprite.get_height() * self.scale_factor))
    #     print(self.coordinate)
        self.set_coordinate(self.reference_rect.center)
        # self.render_text = self.instantiate(TextRender(840,450,self.text, 50, p.Color("white")), self)
        # self.text_rect = self.render_text.rect
        # self.render_text.topleft = self.rect.topleft
        self.render_text = self.instantiate(Text(self.text, 50), self)
        self.render_text.set_anchor((0.5, 0))
        self.render_text.set_pivot((0.5, 0))
        self.render_text.set_margin(top = 50, bottom = 20)
        self.render_text.change_order_layer(20)

        self.retry_button = self.instantiate(RetryButton(960,540,1.25), self)
        self.retry_button.set_anchor((0.5, 1))
        self.retry_button.set_pivot((0.5, 0.5))
        self.retry_button.set_margin(bottom = 100)


        # print(self.unmoved_rect)

        
        # self.on_draw += self.__draw
