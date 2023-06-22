from server.Client import Client
import socket as so

class ClientManager():
    def __init__(self):
        self.clients : list[Client] = []

    def add_client(self, socket : so.socket, address) -> Client:
        client = Client(socket, address)
        self.clients.append(client)
        client.start()
        return client
    
    def stop(self):
        for client in self.clients:
            client.join()

    def unicast(self, receiver : Client, data : str):
        if receiver not in self.clients:
            return

        receiver.socket.send(data.encode())

    def broadcast(self, sender : Client, clients_to_send : list[Client], data : str):
        for client in clients_to_send :
            if client == sender:
                continue

            client.socket.send(data.encode())