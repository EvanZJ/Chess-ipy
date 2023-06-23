import chess
import pygame as p
from item.chess.Board import Board
from item.core.GameObject import GameObject
from item.ui.TextRender import TextRender
from item.ui.popup.NotificationFinished import NotificationFinished
from item.ui.TextButton import TextButton
from item.ui.Text import Text

class Game(GameObject):
    def __init__(self, load_record : list[str] = None):
        super().__init__()
        self.board : Board = None
        self.is_finished : bool = False
        self.on_awake += self.__awake
        self.on_destroy += self.__destroy
        self.on_update += self.__update
        self.on_keyboard_down += self.__on_keyboard_down
        self.close_button = None
        self.relative_value_text : TextRender = None
        self.notif_popup : NotificationFinished = None
        self.load_record : list[str] = load_record

    def __awake(self):
        self.board = Board()
        self.instantiate(self.board)
        self.board.begin()
        self.close_button = self.__create_close_button("Back", 0)
        self.relative_value_text = self.__create_relative_value_text(str(self.board.relative_value)) 
        self.close_button.on_mouse_down += lambda event : self.load_scene(0)

        if self.load_record is not None:
            for move in self.load_record:
                self.board.push(chess.Move.from_uci(move))

    def __destroy(self, game_object : GameObject):
        self.board = None

    def __update(self):
        self.relative_value_text.text = str(self.board.relative_value)
        # self.screen.blit(self.relative_value_text.render(), (0, 0))
        # print(self.relative_value_text.text)
        self.finished = self.board.finished
        # print(self.board.result)

        if self.finished and self.notif_popup is None:
            if self.load_record is not None:
                return
            # self.instantiate(PromotionUI(p.Rect( 0, 0, 800, 600), p.Color(255, 255, 255, 100))))
            self.notif_popup = self.instantiate(NotificationFinished(0,0,2, self.board.result + " wins!"), self)
            self.notif_popup.retry_button.on_mouse_down += lambda event : self.load_scene(1)

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
    
    def __create_relative_value_text(self, text : str) -> TextRender:
        text = self.instantiate(TextRender(
            200,
            100,
            text,
            100,
            p.Color(255, 255, 255, 255),
        ), self)
        return text