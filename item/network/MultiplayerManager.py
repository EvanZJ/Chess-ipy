from item.network.Client import Client
from item.network.CommandHandler import CommandHandler

class MultiplayerManager:
    def __init__(self, client : Client, command_handlers : list[CommandHandler]):
        self.client = client
        self.command_handlers : list[CommandHandler]  = command_handlers
        self.client.on_read_data += self.handle

        self.client.run()

    def handle(self, response : str):
        for command_handler in self.command_handlers:
            if command_handler.handle(response):
                return True
        return False
