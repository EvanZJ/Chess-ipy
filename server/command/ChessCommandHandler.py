from server.Client import Client
from server.ClientManager import ClientManager
from server.CommandHandler import CommandHandler
from server.room.Participant import Participant
from server.room.PieceColor import PieceColor
from server.room.RoomManager import RoomManager

class ChessCommandHandler(CommandHandler):
    def __init__(self, room_manager : RoomManager) -> None:
        super().__init__()

        self.room_manager = room_manager

    def handle(self, sender : Client, client_manager : ClientManager, commands : list[str]) -> bool:
        if commands[0] == "chess":
            if commands[1] == "begin":
                room = self.room_manager.get_room_of_client(sender)
                has_begun = room.begin()
                if has_begun:
                    client_manager.unicast(sender, ["chess", "begin"])
                    client_manager.unicast(room.challenger.client, ["chess", "begin"])
                return has_begun
            if commands[1] == "move":
                room = self.room_manager.get_room_of_client(sender)
                room.chess_board.add_move(commands[2])
                participants = self.room_manager.get_participants_with_client(sender)
                if participants is not None:
                    clients = self.get_clients_from_participants(participants)
                    client_manager.broadcast(sender, clients, commands)
                    return True
                return False
            if commands[1] == "flip":
                room = self.room_manager.get_room_of_client(sender)
                room.switch_room_master_piece_color()
                client_manager.unicast(sender, ["chess", "flip", room.room_master.piece_color.value])
                if room.challenger is not None:
                    client_manager.unicast(room.challenger.client, ["chess", "flip", room.challenger.piece_color.value])
                return True
            if commands[1] == "restart":
                participants = self.room_manager.get_participants_with_client(sender)
                if participants is not None:
                    clients = self.get_clients_from_participants(participants)
                    client_manager.broadcast(sender, clients, commands)
                    return True
                return False
            if commands[1] == "quit":
                participants = self.room_manager.get_participants_with_client(sender)
                if self.room_manager.quit(sender):
                    print(participants)
                    if participants is not None:
                        clients = self.get_clients_from_participants(participants)
                        client_manager.broadcast(sender, clients, commands)
                return True
            if commands[1] == "save":
                room = self.room_manager.get_room_of_client(sender)
                client_manager.unicast(sender, ["chess", "save", room.chess_board.serialize()])
        return False
    
    def get_clients_from_participants(self, participants : list[Participant]):
        clients : list[Client] = []
        for participant in participants:
            clients.append(participant.client)
        return clients