from item.core.GameObject import GameObject
from item.network.Client import Client
from item.network.Room import Room

class MultiplayerGame(GameObject):
    def __init__(self):
        super().__init__()

        self.on_awake += self.__awake

    def __awake(self):
        self.client = Client('localhost')
        self.room = self.instantiate(Room(self.client))
        self.room
