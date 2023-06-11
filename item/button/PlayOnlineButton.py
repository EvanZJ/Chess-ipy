from item.Button import Button
import pygame as p

class PlayOnlineButton(Button):
    def __init__(self, x : float, y : float, scale : float):
        image = p.image.load("resource/images/play_online.png").convert_alpha()
        super().__init__(x, y, image, scale)