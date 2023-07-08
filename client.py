import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
    
    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_command(self, command):
        self.socket.send(command.encode())
        response = self.socket.recv(1024).decode()
        print(response)

    def run(self):
        self.connect()
        while True:
            command = input("Enter a command (or 'quit' to exit): ")
            self.send_command(command)
            if command == "quit":
                break
        self.socket.close()

if __name__ == "__main__":
    client = Client("localhost", 9000)
    client.run()
