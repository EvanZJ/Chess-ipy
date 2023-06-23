import socket as so
import threading

from item.core.Event import Event

SEPERATOR = "<SEPERATOR>"

class Client:
    def __init__(self, host : str, port : int):
        self.socket : so.socket = so.socket(so.AF_INET, so.SOCK_STREAM)
        self.socket.connect((host, port))
        self.threads : list[threading.Thread] = []
        self.buffer_size = 4096

        self.on_read_data = Event()

    def run(self):
        # sendT = threading.Thread(target=self.send)
        # self.threads.append(sendT)
        # sendT.start()
        readT = threading.Thread(target=self.read)
        self.threads.append(readT)
        readT.start()

    def send(self, data : list[str]):
        # while True:
        command = SEPERATOR.join(data)
        self.socket.send(command.encode())
        
    def read(self):
        while True:
            data : str = self.socket.recv(self.buffer_size).decode()
            command = data.split(SEPERATOR)
            self.on_read_data(command)

    def stop(self):
        for thread in self.threads:
            thread.join()