from item.core.GameObject import GameObject
from item.network.Client import Client
from item.network.MultiplayerManager import MultiplayerManager
from item.network.command.ChatCommandHandler import ChatCommandHandler
from item.network.command.ChessCommandHandler import ChessCommandHandler
from item.network.room.Participant import Participant
from item.network.room.Room import Room
from item.network.command.RoomCommandHandler import RoomCommandHandler

class MultiplayerGame(GameObject):
    def __init__(self, user_name, is_join_room : bool = False, room_number = -1):
        super().__init__()

        self.user_name = user_name
        self.is_join_room : bool = is_join_room
        if is_join_room:
            self.room_number = room_number

        self.on_awake += self.__awake

    def __awake(self):
        self.client = Client('localhost', 5000)
        participant = Participant(self.client)
        room = self.instantiate(Room(participant, self.user_name))

        self.command_handlers = [
            RoomCommandHandler(room),
            ChessCommandHandler(participant),
            ChatCommandHandler(participant)
        ]

        self.multiplayer_manager = MultiplayerManager(self.client, self.command_handlers)
        if self.is_join_room:
            room.request_join(self.user_name, self.room_number)
        else:
            room.request_create(self.user_name)
