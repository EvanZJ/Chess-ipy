import json

class Board:
    def __init__(self) -> None:
        self.move_stack : list[str] = []

    def add_move(self, move_uci : str):
        self.move_stack.append(move_uci)

    def serialize(self) -> str:
        json_data = json.dumps(self.move_stack)
        print(json_data)
        return json_data