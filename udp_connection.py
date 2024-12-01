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

    def resolve_udp_addr(self, host: str, port: int) -> tuple:
        ip_addr = socket.gethostbyname(host)
        udp_addr = (ip_addr, port)
        return udp_addr

    def listen_udp(host, port, buffer_size=1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        sock.bind((host, port))
        print(f"Listening on {host}:{port}")
        
        while True:
            data, addr = sock.recvfrom(buffer_size)
            print(f"message sended of {addr}: {data.decode()}")
            
            sock.sendto(f"Response of {host}:{port}".encode(), addr)
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()
