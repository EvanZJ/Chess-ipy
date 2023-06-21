from item.core.Event import Event
from item.core.GameObject import GameObject
from item.network.Client import Client
from item.network.room.PieceColor import PieceColor
from item.network.room.Role import Role

class Participant():
    def __init__(self, client : Client) -> None:
        self.role : Role = Role.WATCHER
        self.piece_color : PieceColor = PieceColor.WHITE
        self.client : Client = client

        self.on_change_piece_color = Event()
        self.on_change_role = Event()

    def change_role(self, new_role : Role):
        self.role = new_role
        self.on_change_role(new_role)

    def change_piece_color(self, new_piece_color : PieceColor):
        self.piece_color = new_piece_color
        self.on_change_piece_color(new_piece_color)