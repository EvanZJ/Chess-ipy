import chess
import pygame as p
from item.Event import Event
from item.GameObject import GameObject
from item.Piece import Piece

class Tile(GameObject):
    def __init__(self, color : p.Color, rect : p.Rect, square : chess.Square):
        super().__init__()
        self.color : p.Color = color
        self.original_color : p.Color = color
        self.rect = rect
        self.square : chess.Square = square
        self.is_legal_move : bool = False

        self.piece : Piece = None

        self.on_select = Event()
        
        self.on_draw += self.__draw
        self.on_mouse_down += self.select

    def __draw(self):
        p.draw.rect(self.screen, self.color, self.rect)
        if(self.is_legal_move):
            p.draw.circle(self.screen, p.Color("grey"), self.rect.center, 10)

    def attach_piece(self, piece : Piece) -> bool:
        if(piece is None):
            return False
        
        self.piece = piece
        piece.move(self.rect.topleft[0], self.rect.topleft[1])
        return True
    
    def select(self):
        self.color = p.Color("yellow")
        self.is_legal_move = False
        self.on_select(self)

    def deselect(self):
        self.color = self.original_color
        self.is_legal_move = False

    def set_legal_move(self, value : bool):
        self.is_legal_move = value
