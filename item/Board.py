import pygame as p
import chess
class Board:
    def __init__(self):
        self.width = 720    
        self.height = 720
        square_size = self.width // 8
        self.max_fps = 60
        self.images = {}
        self.board = chess.Board()
        print(self.board)
        # self.board = self.board.transform(chess.flip_vertical)
        self.convert = {"P": "wp", "R": "wR", "N": "wN", "B": "wB", "Q": "wQ", "K": "wK", "p": "bp", "r": "bR", "n": "bN", "b": "bB", "q": "bQ", "k": "bK"}
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
        self.flipped = True
        self.legal_move_highlighted = []                  
        self.pieces = {}
        self.boxes = []
        self.box_colors = []
        self.load_everything()
        self.box_clicked = None
        self.activated_box = None
        
    def load_everything(self):
        pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
        for piece in pieces:
            self.images[piece] = p.transform.scale(p.image.load("resource/images/piece/" + piece + ".svg"), (self.width // 8, self.height // 8))
        colors = [p.Color("white"), p.Color("purple")]
        for row in range(8):
            for column in range(8):
                color = colors[((row + column) % 2)]
                box = p.Rect(column * self.width // 8, row * self.height // 8, self.width // 8, self.height // 8)
                self.boxes.append(box)
                self.box_colors.append(color)

    def draw(self, screen):
        self.draw_board(screen)
        self.draw_pieces(screen)

    def draw_board(self, screen):
        for row in range(8):
            for column in range(8):
                p.draw.rect(screen, self.box_colors[(row * 8) + column], self.boxes[(row * 8) + column])

    def draw_pieces(self, screen):
        for row in range(8):
            for column in range(8):
                piece = self.board.piece_at(row * 8 + column)
                if piece is not None:
                    if self.flipped:
                        screen.blit(self.images[self.convert[piece.symbol()]], p.Rect((7-column) * self.width // 8, row * self.height // 8, self.width // 8, self.height // 8))
                    else:
                        screen.blit(self.images[self.convert[piece.symbol()]], p.Rect(column * self.width // 8, (7-row) * self.height // 8, self.width // 8, self.height // 8))
                if int(row*8 + column) in self.legal_move_highlighted :
                    # surface = p.Surface((self.width // 8, self.height // 8), p.SRCALPHA)
                    p.draw.circle(screen, p.Color("grey"), (column * self.width // 8 + self.width // 16, row * self.height // 8 + self.height // 16), 10)
                    # screen.blit(surface, (0,0))
    
    def get_clicked_pos(self):
        colors = [p.Color("white"), p.Color("purple")]
        mouse_pos = p.mouse.get_pos()
        for box in self.boxes:
            if box.collidepoint(mouse_pos):
                row = box.y // (self.height // 8)
                column = box.x // (self.width // 8)
                # print(self.white_box_coordinate[row][column])
                if self.box_clicked is None:
                    self.box_clicked = row*8 + column
                    self.activated_box = (row, column)
                    self.box_colors[(row * 8) + column] = p.Color("yellow")
                    return self.white_box_coordinate[row][column] if not self.flipped else self.black_box_coordinate[row][column]
                else :
                    if self.box_clicked == row*8 + column:
                        self.box_clicked = None
                        self.activated_box = None
                        self.box_colors[(row * 8) + column] = colors[((row + column) % 2)]
                    else :
                        self.box_colors[self.box_clicked] = colors[((self.box_clicked // 8 + self.box_clicked % 8) % 2)]
                        self.box_colors[row*8 + column] = p.Color("yellow")
                        self.box_clicked = row*8 + column
                        self.activated_box = (row, column)
                        return self.white_box_coordinate[row][column] if not self.flipped else self.black_box_coordinate[row][column]
        return None
    
    def index_2d(self, v):
        if self.flipped:
            for i, x in enumerate(self.black_box_coordinate):
                if v in x:
                    return (i, x.index(v))
        else :
            for i, x in enumerate(self.white_box_coordinate):
                if v in x:
                    return (i, x.index(v))
    
    def get_piece_legal_moves(self):
        # self.get_clicked_pos()
        selected_uci = self.get_clicked_pos()
        selected_square = chess.parse_square(selected_uci) if selected_uci is not None else None
        print(selected_square, self.activated_box)
        # print(self.get_clicked_pos(), self.box_clicked)
        # selected_square = chess.parse_square(self.get_clicked_pos())
        # print(selected_square)
        # selected_piece = self.board.piece_at(selected_square)
        legal_moves = self.board.legal_moves
        self.legal_move_highlighted = []
        print(legal_moves)
        for move in legal_moves:
            if move.from_square == selected_square:
                index = self.index_2d(chess.square_name(move.to_square))
                indexed = index[0] * 8 + index[1]
                print(index, indexed)
                # print(chess.square_name(move.to_square), self.index_2d(self.white_box_coordinate, chess.square_name(move.to_square)))
                self.legal_move_highlighted.append(indexed)
        print(self.legal_move_highlighted)
            

