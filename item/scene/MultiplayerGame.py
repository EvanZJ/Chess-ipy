from item.core.GameObject import GameObject
from item.network.Client import Client
from item.network.MultiplayerManager import MultiplayerManager
from item.network.Room.Room import Room
from item.network.Room.RoomCommandHandler import RoomCommandHandler

class MultiplayerGame(GameObject):
    def __init__(self, user_name):
        super().__init__()

        self.user_name = user_name

        self.on_awake += self.__awake

    def __awake(self):
        self.client = Client('localhost', 5000)
        room = self.instantiate(Room(self.client, self.user_name))

        self.command_handlers = [
            RoomCommandHandler(room)
        ]

        self.multiplayer_manager = MultiplayerManager(self.client, self.command_handlers)
        room.request_create()
