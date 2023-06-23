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
        self.is_ready : bool = False
        self.has_quit : bool = False

        self.on_change_piece_color = Event()
        self.on_change_role = Event()
        self.on_ready = Event()
        self.on_opponent_move = Event()
        self.on_restart = Event()
        self.on_quit = Event()
        self.on_receive_chat = Event()
        self.on_save = Event()

    def change_role(self, new_role : Role):
        self.role = new_role
        self.on_change_role(new_role)

    def change_piece_color(self, new_piece_color : PieceColor):
        self.piece_color = new_piece_color
        self.on_change_piece_color(new_piece_color)

    def ready(self):
        self.is_ready = True
        self.on_ready()

    def restart(self):
        self.is_ready = False
        self.on_restart()

    def quit(self):
        if not self.has_quit:
            self.has_quit = True
            self.on_quit()

    def receive_chat(self, sender : str, message : str):
        self.on_receive_chat(sender, message)

    def save(self, json : str):
        self.on_save(json)