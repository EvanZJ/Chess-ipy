import chess
import pygame as p
from item.GameObject import GameObject
from item.Piece import Piece
from item.Tile import Tile

class Board(GameObject):
    def __init__(self):
        super().__init__()
        self.width = 720    
        self.height = 720
        self.colors = [p.Color("white"), p.Color("purple")]
        self.board = chess.Board()
        self.convert = {"P": "wp", "R": "wR", "N": "wN", "B": "wB", "Q": "wQ", "K": "wK", "p": "bp", "r": "bR", "n": "bN", "b": "bB", "q": "bQ", "k": "bK"}
        self.tiles : list[Tile] = []
        self.tiles_cache : dict[chess.Square, Tile] = {}
        self.white_box_coordinate = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
                                     ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
                                     ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
                                     ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
                                     ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
                                     ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
                                     ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
                                     ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]
        
        self.on_awake += self.__awake

    def __awake(self):
        for row in range(8):
            for column in range(8):
                tile = self.__instantiate_tile(row, column)
                self.__instantiate_piece(tile, row, column)

    def __instantiate_tile(self, row : int, column : int) -> Tile:
        color = self.colors[((row + column) % 2)]
        box = p.Rect(column * self.width // 8, row * self.height // 8, self.width // 8, self.height // 8)
        square = chess.parse_square(self.white_box_coordinate[row][column])
        tile = self.instantiate(Tile(color, box, square))
        tile.on_select += self.__on_select_piece
        self.tiles.append(tile)
        self.tiles_cache[square] = tile

        return tile

    def __instantiate_piece(self, tile : Tile, row : int, column : int):
        piece = self.board.piece_at(63 - (row * 8 + column))
        if piece is not None:
            symbol = self.convert[piece.symbol()]
            piece_instance = self.instantiate(Piece(piece, symbol))
            piece_instance.scale(self.width // 8, self.height // 8)
            piece_instance.change_order_layer(1)
            tile.attach_piece(piece_instance)

    def __on_select_piece(self, selected_tile : Tile):
        for tile in self.tiles:
            if(tile == selected_tile):
                continue
            tile.deselect()
        for legal_move in self.__get_legal_move(selected_tile):
            legal_move.set_legal_move(True)

    def __get_legal_move(self, tile : Tile) -> list[Tile]:
        legal_moves : list[Tile] = []
        for move in self.board.legal_moves:
            if tile.square == move.from_square:
                legal_moves.append(self.tiles_cache[move.to_square])
        return legal_moves