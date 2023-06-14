import chess
import pygame as p
from item.core.Event import Event
from item.core.GameObject import GameObject
from item.chess.LegalMoveCircle import LegalMoveCircle
from item.chess.Piece import Piece

class Tile(GameObject):
    def __init__(self, color : p.Color, rect : p.Rect, square : chess.Square):
        super().__init__()
        self.color : p.Color = color
        self.original_color : p.Color = color
        self.rect = rect
        self.square : chess.Square = square
        self.legal_move_circle : LegalMoveCircle = None

        self.piece : Piece = None

        self.on_select = Event()
        
        self.on_awake += self.__awake
        self.on_draw += self.__draw
        self.on_mouse_down += self.select
        self.on_destroy += self.__destroy

    def __awake(self):
        self.legal_move_circle = self.instantiate(LegalMoveCircle(self.rect))
        self.legal_move_circle.change_order_layer(2)
        self.legal_move_circle.enabled = False

    def __draw(self):
        p.draw.rect(self.screen, self.color, self.rect)

    def attach_piece(self, piece : Piece) -> bool:
        if(piece is None):
            return False
        
        self.piece = piece
        piece.move(self.rect.topleft[0], self.rect.topleft[1])
        return True
    
    def deattach_piece(self) -> Piece:
        if(self.piece is None):
            return None
        
        deattached_piece = self.piece
        self.piece = None
        return deattached_piece
    
    def select(self):
        self.on_select(self)
        self.set_legal_move(False)

    def highlight(self):
        self.color = p.Color("yellow")

    def deselect(self):
        self.color = self.original_color
        self.set_legal_move(False)

    def set_legal_move(self, value : bool):
        if self.legal_move_circle is None:
            return
        self.legal_move_circle.enabled = value

    def is_legal_move(self) -> bool:
        return self.legal_move_circle.enabled
    
    def destroy_piece(self):
        piece = self.deattach_piece()
        if piece is not None:
            piece.destroy()

    def __destroy(self, game_object : GameObject):
        self.deselect()
        self.destroy_piece()
        if self.legal_move_circle is not None:
            self.legal_move_circle.destroy()
            self.legal_move_circle = None
