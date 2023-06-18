import random

class RoomManager:
    def __init__(self, min_key = 1, max_key = 999999):
        self.occupied_rooms : set = set()
        self.min_key = min_key
        self.max_key = max_key

    def create_room(self) -> int:
        new_room_number = self.generate_unique_key()
        self.occupied_rooms.add(new_room_number)
        return new_room_number

    def join_room(self, room_number : int) -> bool:
        print(room_number)
        return self.occupied_rooms.__contains__(room_number)
    
    def release_room(self, room_number : int):
        if not self.occupied_rooms.__contains__(room_number):
            return
        self.occupied_rooms.remove(room_number)

    def generate_unique_key(self) -> int:
        room_number = random.randint(self.min_key, self.max_key)

        while(room_number in self.occupied_rooms):
            room_number = random.randint(self.min_key, self.max_key)

        return room_number
