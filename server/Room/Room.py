from server.Client import Client
from server.room.PieceColor import PieceColor
from server.room.Participant import Participant
from server.room.Role import Role

class Room:
    def __init__(self, key : int, room_master : Participant) -> None:
        self.key : int = key
        self.room_master : Participant = room_master
        self.challenger : Participant = None
        self.participants : list[Participant] = []
        self.participants.append(self.room_master)
        self.has_begun : bool = False

    def add_participant(self, participant : Participant):
        if self.room_master != participant:
            if participant.role == Role.PLAYER:
                participant.switch_piece_color(self.room_master.piece_color)
                self.challenger = participant
        self.participants.append(participant)

    def is_client_in_participants(self, client : Client) -> bool:
        for participant in self.participants:
            if participant.client == client:
                return True
        return False
    
    def switch_room_master_piece_color(self):
        self.room_master.switch_piece_color(self.room_master.piece_color)

        if self.challenger is not None:
            self.challenger.switch_piece_color(self.room_master.piece_color)
    
    def get_participants(self) -> list[Participant]:
        return self.participants
    
    def begin(self) -> bool:
        if not isinstance(self.room_master, Participant):
            return False
        if self.challenger is None:
            return False
        self.has_begun = True
        return True