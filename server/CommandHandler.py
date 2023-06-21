from abc import ABC, abstractmethod

from server.Client import Client
from server.ClientManager import ClientManager

class CommandHandler(ABC):
    @abstractmethod
    def handle(self, sender : Client, client_manager : ClientManager, command : str) -> bool:
        pass