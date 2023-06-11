from item.core.GameObject import GameObject
import chess
import pygame as p

class Piece(GameObject):
    def __init__(self, piece : chess.Piece, symbol : str):
        super().__init__()
        self.piece : chess.Piece = piece
        self.symbol : str = symbol
        self.sprite = p.image.load("resource/images/piece/" + symbol + ".svg")