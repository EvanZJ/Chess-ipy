from server.CommandHandler import CommandHandler
from server.Room.RoomManager import RoomManager

class RoomCommandHandler(CommandHandler):
    def __init__(self) -> None:
        super().__init__()

        self.room_manager = RoomManager()

    def Handle(self, command : str) -> bool:
        commands = command.split(" ")
        if commands[0] == "room":
            if commands[1] == "create":
                self.room_manager.create_room()
                return True 
            if commands[1] == "join":
                self.room_manager.join_room((int)command[2])
                return True
            if commands[1] == "release":
                self.room_manager.release_room((int)commands[2])
                return True
        return False