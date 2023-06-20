import socket as so

import pygame as p
from item.chess.Board import Board

from item.core.GameObject import GameObject
from item.network.Client import Client
from item.network.Room.RoomDetail import RoomDetail
from item.ui.Text import Text

class Room(GameObject):
    def __init__(self, client : Client, user_name : str):
        super().__init__()

        self.client : Client = client
        self.user_name : str = user_name

    def request_create(self, user_name : str):
        self.client.send("room create " + user_name)

    def request_join(self, user_name : str, room_number : int):
        self.client.send("room join " + room_number + " " + user_name)

    def create(self, room_number : int):
        self.instantiate(Board())
        self.instantiate(RoomDetail(p.Rect(1150, 70, 200, 600), room_number, self.user_name))