from item.T.Button import Button
import pygame as p

from item.T.scene.Game import Game

class PlayLocalButton(Button):
    def __init__(self, x : float, y : float, scale : float):
        image = p.image.load("resource/images/play_now.png").convert_alpha()
        super().__init__(x, y, image, scale)

        self.on_mouse_down += self.play

    def play(self):
        self.load(Game())