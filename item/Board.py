import pygame as p
import chess
class Board:
    def __init__(self):
        self.width = 720    
        self.height = 720
        square_size = self.width // 8
        self.max_fps = 60
        self.images = {}
        self.load_images()
        self.board = chess.Board()
        self.convert = {"P": "wp", "R": "wR", "N": "wN", "B": "wB", "Q": "wQ", "K": "wK", "p": "bp", "r": "bR", "n": "bN", "b": "bB", "q": "bQ", "k": "bK"}
        self.pieces = {}
        self.boxes = []
    def load_images(self):
        pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
        for piece in pieces:
            self.images[piece] = p.transform.scale(p.image.load("resource/images/piece/" + piece + ".svg"), (self.width // 8, self.height // 8))
    
    def draw(self, screen):
        self.draw_board(screen)
        self.draw_pieces(screen)

    def draw_board(self, screen):
        colors = [p.Color("white"), p.Color("purple")]
        for row in range(8):
            for column in range(8):
                color = colors[((row + column) % 2)]
                box = p.Rect(column * self.width // 8, row * self.height // 8, self.width // 8, self.height // 8)
                self.boxes.append(box)
                p.draw.rect(screen, color, box)

    def draw_pieces(self, screen):
        for row in range(8):
            for column in range(8):
                piece = self.board.piece_at(row * 8 + column)
                if piece is not None:
                    the_piece = self.convert[piece.symbol()]
                    screen.blit(self.images[self.convert[piece.symbol()]], p.Rect(column * self.width // 8, row * self.height // 8, self.width // 8, self.height // 8))
    
    def get_clicked_pos(self):
        mouse_pos = p.mouse.get_pos()
        for box in self.boxes:
            if box.collidepoint(mouse_pos):
                row = box.y // (self.height // 8)
                column = box.x // (self.width // 8)
                print(row, column)
                return row, column
        return None

