from collections import deque
import chess
import pygame as p
from item.core.GameObject import GameObject
from item.chess.Piece import Piece
from item.chess.Tile import Tile

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
        self.current_selected_tile : Tile = None
        self.last_move_tile : Tile = []
        self.move_stack : deque[chess.Move] = deque()
        self.white_box_coordinate = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
                                     ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
                                     ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
                                     ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
                                     ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
                                     ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
                                     ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
                                     ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]
        self.black_box_coordinate = [["h1", "g1", "f1", "e1", "d1", "c1", "b1", "a1"],
                                     ["h2", "g2", "f2", "e2", "d2", "c2", "b2", "a2"],
                                     ["h3", "g3", "f3", "e3", "d3", "c3", "b3", "a3"],
                                     ["h4", "g4", "f4", "e4", "d4", "c4", "b4", "a4"],
                                     ["h5", "g5", "f5", "e5", "d5", "c5", "b5", "a5"],
                                     ["h6", "g6", "f6", "e6", "d6", "c6", "b6", "a6"],
                                     ["h7", "g7", "f7", "e7", "d7", "c7", "b7", "a7"],
                                     ["h8", "g8", "f8", "e8", "d8", "c8", "b8", "a8"]]
        infoObject = p.display.Info()
        self.current_width = infoObject.current_w
        self.current_height = infoObject.current_h
        self.on_awake += self.__awake
        self.on_keyboard_down += self.__on_keyboard_down
        self.relative_value = 0
        self.flipped : bool = False
        self.finished : bool = False
        # self.on_update += self.__update

    def __awake(self):
        for row in range(8):
            for column in range(8):
                tile = self.__instantiate_tile(row, column)
                piece = self.board.piece_at(tile.square)
                self.__instantiate_piece(tile, piece)

    def __on_keyboard_down(self, event : p.event.Event):
        if event.key == p.K_LEFT:
            if len(self.board.move_stack) > 0:
                self.move_stack.append(self.board.pop())
                self.__redraw()
        if event.key == p.K_RIGHT:
            if len(self.move_stack) > 0:
                self.board.push(self.move_stack.pop())
                self.__redraw()
        if event.key == p.K_f:
            print('sini')
            self.__flip_board()
            # self.__redraw()
            

    def __redraw(self):
        # print("redraw")
        for tile in self.tiles:
            tile.destroy()
        self.tiles_cache.clear()
        self.tiles.clear()
        for row in range(8):
            for column in range(8):
                tile = self.__instantiate_tile(row, column)
                self.tiles.append(tile)
                self.tiles_cache[tile.square] = tile

                piece = self.board.piece_at(tile.square)
                
                if piece is not None:
                    self.__instantiate_piece(tile, piece)

        self.relative_value = self.__get_relative_value()
        self.finished = self.board.is_game_over()
        print(self.relative_value)
        
        # for square in self.last_move_tile:
        #     self.tiles_cache[square].color = p.Color("yellow")

    def __instantiate_tile(self, row : int, column : int) -> Tile:
        color = self.colors[((row + column) % 2)]
        box = p.Rect(
            (column * self.width // 8) + ((self.current_width - self.width) / 2),
            (row * self.height // 8) + ((self.current_height - self.height) / 2),
            self.width // 8,
            self.height // 8
        )
        
        square = chess.parse_square(self.white_box_coordinate[row][column]) if not self.flipped else chess.parse_square(self.black_box_coordinate[row][column])
        if square in self.last_move_tile:
            color = p.Color("green")

        tile = self.instantiate(Tile(color, box, square))

        tile.on_select += self.__on_select_tile
        self.tiles.append(tile)
        self.tiles_cache[square] = tile

        return tile

    def __instantiate_piece(self, tile : Tile, piece : chess.Piece):
        if piece is not None:
            symbol = self.convert[piece.symbol()]
            piece_instance = self.instantiate(Piece(piece, symbol))
            piece_instance.scale(self.width // 8, self.height // 8)
            piece_instance.change_order_layer(1)
            tile.attach_piece(piece_instance)

    def __on_select_tile(self, selected_tile : Tile):
        if not self.__can_interact_with_board():
            return

        selected_tile.highlight()

        if selected_tile.is_legal_move():
            self.__move_piece(selected_tile)

        self.current_selected_tile = selected_tile
        for tile in self.tiles:
            if(tile == selected_tile):
                continue
            if tile in self.last_move_tile:
                continue
            tile.deselect()
        for tile in self.__get_legal_move(selected_tile):
            tile.set_legal_move(True)

    def __get_legal_move(self, tile : Tile) -> list[Tile]:
        legal_moves : list[Tile] = []
        for move in self.board.legal_moves:
            if tile.square == move.from_square:
                legal_moves.append(self.tiles_cache[move.to_square])
        return legal_moves
    
    def __move_piece(self, to_tile : Tile):
        move_piece = chess.Move(self.current_selected_tile.square, to_tile.square)

        if self.__is_promotion(self.current_selected_tile.piece, move_piece):
            move_piece.promotion = chess.QUEEN
            
        self.last_move_tile.clear()
        self.last_move_tile.append(self.current_selected_tile.square)
        self.last_move_tile.append(to_tile.square)
        self.board.push(move_piece)
        self.__redraw()

    def __can_interact_with_board(self) -> bool:
        return len(self.move_stack) <= 0
    
    def __get_relative_value(self) -> int :
        relative_value = 0
        for tile in self.tiles_cache.values():
            piece = tile.piece
            if piece is not None:
                if piece.piece.color == chess.WHITE:
                    relative_value += self.__get_piece_value(piece)
                else:
                    relative_value -= self.__get_piece_value(piece)
        return relative_value

    def __get_piece_value(self, piece : chess.Piece) -> int:
        if piece.piece.piece_type == chess.PAWN:
            return 1
        elif piece.piece.piece_type == chess.KNIGHT:
            return 3
        elif piece.piece.piece_type == chess.BISHOP:
            return 3
        elif piece.piece.piece_type == chess.ROOK:
            return 5
        elif piece.piece.piece_type == chess.QUEEN:
            return 9
        elif piece.piece.piece_type == chess.KING:
            return 0
        else:
            return 0
        
    def __flip_board(self):
        self.flipped = not self.flipped
        self.__redraw()

    def __is_promotion(self, piece : Piece, move : chess.Move) -> bool:
        last_rank = 7 if self.board.turn == chess.WHITE else 0
        if piece.get_piece_type() != chess.PAWN:
            return False
        return chess.square_rank(move.to_square) == last_rank
    
    
