import socket

class UDPConnection:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = (host, port)
        self.socket.bind(self.address)

    def send(self, data):
        self.socket.sendto(data.encode(), self.address)

    def receive(self):
        data, addr = self.socket.recvfrom(1024)
        return data.decode()

    def close(self):
        self.socket.close()
