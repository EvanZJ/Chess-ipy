import socket as so

import pygame as p

from item.core.GameObject import GameObject
from item.network.chess.MultiplayerBoard import MultiplayerBoard
from item.network.room.Participant import Participant
from item.network.room.PieceColor import PieceColor
from item.network.room.Role import Role
from item.network.room.RoomDetail import RoomDetail

class Room(GameObject):
    def __init__(self, participant : Participant, user_name : str):
        super().__init__()

        self.participant : Participant = participant
        self.user_name : str = user_name

    def request_create(self, user_name : str):
        print("Username: " + user_name)
        self.participant.client.send("room create " + user_name)

    def request_join(self, user_name : str, room_number : int):
        self.participant.client.send("room join " + room_number + " " + user_name)

    def create(self, room_number : int):
        print("a")
        self.participant.change_role(Role.ROOMMASTER)
        self.instantiate(MultiplayerBoard(self.participant))
        self.participant.change_piece_color(PieceColor.WHITE)
        self.instantiate(RoomDetail(p.Rect(1200, 90, 200, 600), room_number, self.user_name))

    def join(self, room_number : int):
        print("b")
        self.participant.change_role(Role.CHALLENGER)
        self.instantiate(MultiplayerBoard(self.participant))
        self.participant.change_piece_color(PieceColor.BLACK)
        self.instantiate(RoomDetail(p.Rect(1200, 90, 200, 600), room_number, self.user_name))