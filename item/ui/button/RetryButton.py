import pygame as p
from item.ui.ImageButton import ImageButton
from item.core.Event import Event
class RetryButton(ImageButton):
    def __init__(self, x : int, y : int, scale : float):
        image = p.image.load("resource/images/retry.png")
        super().__init__(x, y, image, scale)
        self.order_layer = 5
    
        # self.on_mouse_down += self.retry
