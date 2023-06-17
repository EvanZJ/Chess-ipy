import socket as so

from item.core.GameObject import GameObject
from item.network.Client import Client

class Room(GameObject):
    def __init__(self, client : Client):
        self.client : Client = client

    def create(self):
        self.client.send("room create")

    def join(self, room_number : int):
        self.client.send("room join " + room_number)