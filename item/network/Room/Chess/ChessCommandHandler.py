from item.network.CommandHandler import CommandHandler

class ChessCommandHandler(CommandHandler):
    def __init__(self) -> None:
        super().__init__()

    def Handle(self, command : str) -> bool:
        commands = command.split(" ")
        print(command)
        if commands[0] == "chess":
            if commands[1] == "move":
                return True
        return False