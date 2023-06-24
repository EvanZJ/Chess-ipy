from server.Client import Client
from server.ClientManager import ClientManager
from server.CommandHandler import CommandHandler
from server.room.Participant import Participant
from server.room.PieceColor import PieceColor
from server.room.RoomManager import RoomManager

class ChatCommandHandler(CommandHandler):
    def __init__(self, room_manager : RoomManager) -> None:
        super().__init__()

        self.room_manager = room_manager

    def handle(self, sender : Client, client_manager : ClientManager, commands : list[str]) -> bool:
        if commands[0] == "chat":
            if commands[1] == "sendall":
                participants = self.room_manager.get_participants_with_client(sender)
                if participants is not None:
                    clients = self.get_clients_from_participants(participants)
                    client_manager.broadcast(sender, clients, commands)
                    return True
                return False
        return False
    
    def get_clients_from_participants(self, participants : list[Participant]):
        clients : list[Client] = []
        for participant in participants:
            clients.append(participant.client)
        return clients