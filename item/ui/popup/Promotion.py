import pygame as p
import chess
from item.chess.Piece import Piece
from item.chess.Tile import Tile
from item.core.GameObject import GameObject
from item.ui.UI import UI
from item.core.Event import Event


class PromotionUI(GameObject):
    def __init__(self, rect : p.Rect = None, color : p.Color = p.Color("white"), turn : str = "white", square : chess.Square = None):
        super().__init__()
        self.white_piece = ["Q", "R", "N", "B"]
        self.convert = {"P": "wp", "R": "wR", "N": "wN", "B": "wB", "Q": "wQ", "K": "wK", "p": "bp", "r": "bR", "n": "bN", "b": "bB", "q": "bQ", "k": "bK"}
        self.black_piece = ["r", "n", "b", "q"]
        self.turn = turn
        self.tiles : Tile = []
        self.rect = rect
        self.color = color
        self.on_select = Event()
        self.square = square
        # print(rect, color)
        self.order_layer = 100
        self.on_awake += self.__awake
        self.selected_piece = None
        self.piece_convert = {"Q": chess.QUEEN, "R": chess.ROOK, "N": chess.KNIGHT, "B": chess.BISHOP}
        # self.on_draw += self.__draw
        # screen fill with black
        # self.screen.fill(p.Color("black"))
        
    
    def __awake(self):
        for i in range(4):
            tile = self.instantiate(Tile(self.color, p.Rect(self.rect.topleft[0], self.rect.topleft[1] + i * self.rect.width, self.rect.width, self.rect.width), None), self)
            tile.change_order_layer(101)
            tile.square = self.square
            # tile.on_mouse_down += self.__select
            self.tiles.append(tile)
            c_piece = chess.Piece(self.piece_convert[self.white_piece[i]], True if self.turn == "white" else False)
            piece = self.instantiate(Piece(c_piece, self.convert[self.white_piece[i]]), tile) if self.turn == "white" else self.instantiate(Piece(c_piece, self.convert[self.black_piece[i]]), tile)
            piece.change_order_layer(102)
            piece.scale(self.rect.width, self.rect.height // 4)
            tile.attach_piece(piece)
            tile.on_select += self.__on_select_tile
            
    def __select(self):
        self.on_select(self)

    def __on_select_tile(self, selected_tile : Tile):
        # print(selected_tile.piece.piece)
        # return self.piece_convert[selected_tile.piece.piece]
        self.on_select(selected_tile.piece.get_piece_type())
        # return symbol