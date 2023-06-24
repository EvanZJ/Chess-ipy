from server.Client import Client
from server.ClientManager import ClientManager
from server.CommandHandler import CommandHandler
from server.room.Participant import Participant
from server.room.Role import Role
from server.room.RoomManager import RoomManager

class RoomCommandHandler(CommandHandler):
    def __init__(self, room_manager : RoomManager) -> None:
        super().__init__()

        self.room_manager = room_manager

    def handle(self, sender : Client, client_manager : ClientManager, commands : list[str]) -> bool:
        if commands[0] == "room":
            if commands[1] == "create":
                new_room_number = self.room_manager.create_room(Participant(commands[2], sender))
                print("Room created successfully : " + str(new_room_number))
                client_manager.unicast(sender, ["room", "create", str(new_room_number)])
                return True 
            if commands[1] == "join":
                role = Role.PLAYER
                if commands[4] == "watcher":
                    role = Role.WATCHER
                if self.room_manager.join_room(int(commands[2]), Participant(commands[3], sender, role)):
                    client_manager.unicast(sender, ["room", "join", str(commands[2])])
                    return True
                client_manager.unicast(sender, ["room", "error", f"Room with key: {commands[2]} is not found."])
                return False
            if commands[1] == "release":
                self.room_manager.release_room(int(commands[2]))
                return True
        return False