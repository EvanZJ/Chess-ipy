import pygame as p
from item.Board import Board
from item.GameObject import GameObject

class Game(GameObject):
    def __init__(self):
        super().__init__()

        self.on_awake += self.__awake

    def __awake(self):
        self.instantiate(Board())