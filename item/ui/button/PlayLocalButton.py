from item.ui.ImageButton import ImageButton
import pygame as p

class PlayLocalButton(ImageButton):
    def __init__(self, x : float, y : float, scale : float):
        image = p.image.load("resource/images/play_now.png").convert_alpha()
        super().__init__(x, y, image, scale)