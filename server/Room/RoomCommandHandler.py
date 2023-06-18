from server.Client import Client
from server.ClientManager import ClientManager
from server.CommandHandler import CommandHandler
from server.Room.RoomManager import RoomManager

class RoomCommandHandler(CommandHandler):
    def __init__(self) -> None:
        super().__init__()

        self.room_manager = RoomManager()

    def Handle(self, sender : Client, client_manager : ClientManager, command : str) -> bool:
        commands = command.split(" ")
        if commands[0] == "room":
            if commands[1] == "create":
                new_room_number = self.room_manager.create_room()
                print("Room created successfully : " + str(new_room_number))
                client_manager.unicast(sender, "room create " + str(new_room_number))
                return True 
            if commands[1] == "join":
                if self.room_manager.join_room(int(commands[2])):
                    client_manager.unicast(sender, "room join " + str(commands[2]))
                    return True
                return False
            if commands[1] == "release":
                self.room_manager.release_room(int(commands[2]))
                return True
        return False