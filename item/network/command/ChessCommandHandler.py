from item.network.CommandHandler import CommandHandler
from item.network.room.Participant import Participant
from item.network.room.PieceColor import PieceColor

class ChessCommandHandler(CommandHandler):
    def __init__(self, participant : Participant) -> None:
        super().__init__()

        self.participant = participant

    def handle(self, command : str) -> bool:
        commands = command.split(" ")
        print(command)
        if commands[0] == "chess":
            if commands[1] == "begin":
                self.participant.ready()
                return True
            if commands[1] == "move":
                self.participant.on_opponent_move(commands[2])
                return True
            if commands[1] == "flip":
                if commands[2] == "white":
                    self.participant.change_piece_color(PieceColor.WHITE)
                elif commands[2] == "black":
                    self.participant.change_piece_color(PieceColor.BLACK)
        return False