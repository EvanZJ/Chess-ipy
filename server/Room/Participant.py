from server.Client import Client
from server.room.PieceColor import PieceColor
from server.room.Role import Role

class Participant:
    def __init__(self, name : str, client : Client, role : Role = Role.PLAYER, piece_color : PieceColor = PieceColor.WHITE):
        self.name : str = name
        self.client : Client = client
        self.role : Role = role
        self.piece_color : PieceColor = piece_color

    def set_role(self, new_role : Role):
        self.role = new_role

    def switch_piece_color(self):
        if self.piece_color == PieceColor.WHITE:
            self.piece_color = PieceColor.BLACK
        elif self.piece_color == PieceColor.BLACK:
            self.piece_color = PieceColor.WHITE

    def set_piece_color(self, new_piece_color : PieceColor):
        self.piece_color = new_piece_color