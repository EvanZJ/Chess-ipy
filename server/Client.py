import threading
import socket as so

from server.Event import Event

class Client(threading.Thread):
    def __init__(self, socket : so.socket, address):
        threading.Thread.__init__(self)
        self.socket : so.socket = socket
        self.address = address
        self.size = 4096

        self.on_receive_data = Event()

    def run(self):
        running = 1
        while running:
            data = self.socket.recv(self.size).decode()
            self.on_receive_data(self, data)
                

