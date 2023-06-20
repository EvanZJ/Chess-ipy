from server.Client import Client
from server.room.Participant import Participant
from server.room.Role import Role

class Room:
    def __init__(self, key : int, room_master : Participant) -> None:
        self.key : int = key
        self.room_master : Participant = room_master
        self.participants : list[Participant] = []
        self.participants.append(self.room_master)

    def add_participant(self, participant : Participant):
        if self.room_master != participant:
            if participant.role == Role.PLAYER:
                if participant.piece_color == self.room_master.piece_color:
                    participant.switch_piece_color()
        self.participants.append(participant)

    def is_client_in_participants(self, client : Client) -> bool:
        for participant in self.participants:
            if participant.client == client:
                return True
        return False
    
    def get_participants(self) -> list[Participant]:
        return self.participants