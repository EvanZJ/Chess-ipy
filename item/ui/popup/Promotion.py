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

            # self.pieces.append(self.instantiate(Piece(self.white_piece[i], self.convert[self.white_piece[i]], True))) if self.turn == "white" else self.pieces.append(self.instantiate(Piece(self.black_piece[i], self.convert[self.black_piece[i]], True)))
            # self.pieces[i].change_order_layer(101)
            # self.pieces[i].move(self.rect.topleft[0], self.rect.topleft[1] + i * self.rect.width)
            # self.pieces[i].scale(self.rect.width, self.rect.height // 4)
            # self.on_mouse_down += self.__mouse_down

    #     self.scale(int(self.sprite.get_width() * self.scale_xy), int(self.sprite.get_height() * self.scale_xy))
    #     self.move(self.current_width/2 - self.rect.width/2, self.current_height/2 - self.rect.height/2)
        

        # self.piece = self.white_piece
        # self.on_mouse_down += self.__mouse_down

    # def __draw(self):
        # p.draw.rect(self.screen, self.color, self.rect)

    def __mouse_down(self):
        # get piece symbol if mouse button down
        for event in p.event.get():
            if event.type == p.MOUSEBUTTONDOWN:
                mouse_pos = p.mouse.get_pos()
                for piece in self.pieces:
                    if piece.rect.collidepoint(mouse_pos):
                        print(piece.symbol)
                        # return piece.symbol

    def __select(self):
        self.on_select(self)

    def __on_select_tile(self, selected_tile : Tile):
        # print(selected_tile.piece.piece)
        # return self.piece_convert[selected_tile.piece.piece]
        self.on_select(selected_tile.piece.get_piece_type())
        # return symbol