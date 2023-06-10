import pygame as p
from item.T.GameObject import GameObject

class Game(GameObject):
    def __init__(self):
        super().__init__()

        self.on_start += self.start

    def start(self):
        self.screen.fill((0, 0, 0))