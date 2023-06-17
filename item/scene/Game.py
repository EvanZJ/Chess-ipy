import pygame as p
from item.chess.Board import Board
from item.core.GameObject import GameObject
from item.ui.popup.NotificationFinished import NotificationFinished
from item.ui.TextButton import TextButton

class Game(GameObject):
    def __init__(self):
        super().__init__()
        self.board : Board = None
        self.is_finished : bool = False
        self.on_awake += self.__awake
        self.on_destroy += self.__destroy
        self.on_update += self.__update
        self.on_keyboard_down += self.__on_keyboard_down
        self.close_button = None

    def __awake(self):
        self.board = Board()
        self.instantiate(self.board)
        self.close_button = self.__create_close_button("Back", 0)
        self.close_button.on_mouse_down += lambda : self.load_scene(0)

    def __destroy(self, game_object : GameObject):
        self.board = None

    def __update(self):
        self.finished = self.board.finished
        if self.finished:
            # self.instantiate(PromotionUI(p.Rect( 0, 0, 800, 600), p.Color(255, 255, 255, 100))))
            self.instantiate(NotificationFinished(0,0,2))

    def __on_keyboard_down(self, event : p.event.Event):
        if event.key == p.K_ESCAPE:
            self.load_scene(0)
            
    def __create_close_button(self, text : str, top_margin : int) -> TextButton:
        button = self.instantiate(TextButton(
            p.Rect(0, 0, 280, 100),
            p.Color(0, 0, 0, 255),
            0,
            text = text, 
            text_size = 48
        ), self)
        button.set_anchor((0.5, 0))
        button.set_pivot((0, 0))
        button.set_margin(top = top_margin)
        
        return button