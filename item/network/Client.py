import socket as so
import threading

from item.core.Event import Event

class Client:
    def __init__(self, server_address : so._Address):
        self.socket : so.socket = so.socket(so.AF_INET, so.SOCK_STREAM)
        self.socket.connect(server_address)
        self.threads : list[threading.Thread] = []
        self.buffer_size = 4096

        self.on_read_data = Event()

    def run(self):
        sendT = threading.Thread(target=self.send)
        self.threads.append(sendT)
        sendT.start()
        readT = threading.Thread(target=self.read)
        self.threads.append(readT)
        readT.start()

    def send(self, data : str):
        while True:
            self.socket.send(data)
        
    def read(self):
        while True:
            data : str = self.socket.recv(self.buffer_size).decode()
            self.on_read_data(data)

    def stop(self):
        for thread in self.threads:
            thread.join()