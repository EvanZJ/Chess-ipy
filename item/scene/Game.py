import pygame as p
from item.chess.Board import Board
from item.core.GameObject import GameObject
from item.ui.popup.NotificationFinished import NotificationFinished

class Game(GameObject):
    def __init__(self):
        super().__init__()
        self.board : Board = None
        self.is_finished : bool = False
        self.on_awake += self.__awake
        self.on_destroy += self.__destroy
        self.on_update += self.__update

    def __awake(self):
        self.board = Board()
        self.instantiate(self.board)

    def __destroy(self):
        self.board = None

    def __update(self):
        self.finished = self.board.finished
        if self.finished:
            self.instantiate(NotificationFinished(0,0,1))