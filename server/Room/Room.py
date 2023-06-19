class Room:
    def __init__(self, key : int, room_master : str) -> None:
        self.key : int = key
        self.room_master : str = room_master
        self.participants : list[str] = []
        self.participants.append(self.room_master)

    def add_participant(self, participant : str):
        self.participants.append(participant)