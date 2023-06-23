from item.network.CommandHandler import CommandHandler
from item.network.room.Participant import Participant
from item.network.room.PieceColor import PieceColor

class ChatCommandHandler(CommandHandler):
    def __init__(self, participant : Participant) -> None:
        super().__init__()

        self.participant = participant

    def handle(self, commands : list[str]) -> bool:
        print(commands)
        if commands[0] == "chat":
            if commands[1] == "sendall":
                self.participant.receive_chat(commands[2], commands[3])
                return True
        return False