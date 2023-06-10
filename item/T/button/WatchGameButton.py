from item.T.Button import Button
import pygame as p

class WatchGameButton(Button):
    def __init__(self, x : float, y : float, scale : float):
        image = p.image.load("resource/images/watch_match.png").convert_alpha()
        super().__init__(x, y, image, scale)