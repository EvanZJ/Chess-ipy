import random
from server.Client import Client
from server.room.Participant import Participant
from server.room.Room import Room

class RoomManager:
    def __init__(self, min_key = 1, max_key = 999999):
        self.occupied_rooms : dict[int, Room] = {}
        self.min_key = min_key
        self.max_key = max_key

    def create_room(self, room_master : Participant) -> int:
        new_room_number = self.generate_unique_key()
        new_room = Room(new_room_number, room_master)
        self.occupied_rooms[new_room_number] = new_room
        return new_room_number

    def join_room(self, room_number : int, participant : Participant) -> bool:
        print(room_number)
        if room_number in self.occupied_rooms.keys():
            self.occupied_rooms[room_number].add_participant(participant)
        return room_number in self.occupied_rooms.keys()
    
    def release_room(self, room_number : int):
        if room_number not in self.occupied_rooms.keys():
            return
        self.occupied_rooms.pop(room_number)

    def generate_unique_key(self) -> int:
        room_number = random.randint(self.min_key, self.max_key)

        while(room_number in self.occupied_rooms.keys()):
            room_number = random.randint(self.min_key, self.max_key)

        return room_number
    
    def get_participants_with_client(self, client_to_search : Client) -> list[Participant] | None:
        for room in self.occupied_rooms.values():
            if room.is_client_in_participants(client_to_search):
                return room.get_participants()
        return None
