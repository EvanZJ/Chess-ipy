from item.core.GameObject import GameObject
import chess
import pygame as p

class Piece(GameObject):
    def __init__(self, piece : chess.Piece, symbol : str):
        super().__init__()
        self.piece : chess.Piece = piece
        self.symbol : str = symbol
        self.sprite = p.image.load("resource/images/piece/" + symbol + ".svg")
        self.block_raycast = False
        # self.press_enabled = press_enabled
        # self.on_mouse_down += self.mouse_down
        

    def get_piece_type(self) -> chess.PieceType:
        return self.piece.piece_type
    
# def mouse_down(self):
#         if self.press_enabled:
#             print(self.symbol)