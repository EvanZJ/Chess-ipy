from item.network.CommandHandler import CommandHandler
from item.network.room.Room import Room

class RoomCommandHandler(CommandHandler):
    def __init__(self, room : Room) -> None:
        super().__init__()

        self.room = room

    def handle(self, commands : list[str]) -> bool:
        print(commands)
        if commands[0] == "room":
            if commands[1] == "create":
                self.room.create(int(commands[2]))
                return True
            if commands[1] == "join":
                self.room.join(int(commands[2]))
                return True
            if commands[1] == "error":
                self.room.error(commands[2])
                print(commands[2])
                return True
        return False