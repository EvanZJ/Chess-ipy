from item.chess.Board import Board
from item.network.room.Participant import Participant
from item.network.room.PieceColor import PieceColor
from item.network.room.Role import Role

class MultiplayerBoard(Board):
    def __init__(self, participant : Participant):
        super().__init__()

        self.participant : Participant = participant
        self.participant.on_change_piece_color += self.__on_change_piece_color
        self.on_flip_board += self.__on_flip_board

    def __on_change_piece_color(self, new_piece_color : PieceColor):
        if self.flipped == False and new_piece_color == PieceColor.BLACK:
            self.flip_board()
        elif self.flipped == True and new_piece_color == PieceColor.WHITE:
            self.flip_board()

    def __on_flip_board(self):
        if self.participant.role != Role.ROOMMASTER:
            return

        self.participant.client.send("chess flip")
