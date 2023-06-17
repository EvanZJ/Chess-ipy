import select as se
import socket as so
import sys
import threading
import struct

from server.Client import Client
from server.CommandHandler import CommandHandler
from server.Room.RoomCommandHandler import RoomCommandHandler

class Server:
    def __init__(self, host : str, port : int, listen : int, command_handlers : list[CommandHandler]):
        self.host : str = host
        self.port : int = port
        self.listen : int = listen
        self.clients : list[Client] = []
        self.command_handlers : list[CommandHandler] = command_handlers

    def open_socket(self):
        self.server = so.socket(so.AF_INET, so.SOCK_STREAM)
        self.server.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, 1)
        self.server.bind((self.host,self.port))
        self.server.listen(self.listen)

    def run(self):
        self.open_socket()
        input = [self.server]
        running = 1
        while running:
            inputready, outputready, exceptready = se.select(input, [], [])

            for s in inputready:
                if s == self.server:
                    client_socket, client_address = self.server.accept()
                    client = Client(client_socket, client_address)
                    client.on_receive_data += self.handle_data
                    client.start()
                    self.clients.append(client)
        self.server.close()
        for client in self.clients:
            client.join()

    def handle_data(self, receiving_client : Client, data : str):
        for command_handler in self.command_handlers:
            if command_handler.Handle(data):
                print("command executed success")
        print("command executed failed")

    def broadcast(self, sender : Client, data : str):
        for client in self.clients :
            if client == sender:
                continue

            client.socket.send(data.encode())

command_handlers : list[CommandHandler] = {
    RoomCommandHandler()
}
s = Server('localhost', 5000, 50, command_handlers)
s.run()