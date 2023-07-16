import socket


class Server:
    def __init__(self):
        self.server_ip = "127.0.0.1"
        self.server_port = 6969
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.server_ip, self.server_port))
        self.room = {}  # int : []

    def listen(self):
        while True:
            data, client_address = self.server_socket.recvfrom(1024)
            message = data.decode('utf-8')
            print(f"Received message: {message} from {client_address}")
            self.command(message, client_address)

    def command(self, command: str, client_address):
        if command.startswith("connectroom_"):
            room_number = command.split("_")[1]

            # We check if the room already exists or not
            if room_number in self.room:
                self.lobby_join(client_address, room_number)
            else:
                self.lobby_join(client_address, room_number, create_new_lobby=True)

        # Receies chat message from server. Forwards the chatmessage to all clients in lobby except the sender
        # Format: ChatMessage_playernumber_lobbynumber_message

        if command.startswith("ChatMessage"):
            # iterates over all room numbers
            lobby_number = command.split("_")[2]
            player_number = command.split("_")[1]

            for index, player in enumerate(self.room.get(lobby_number)):
                if index + 1 != int(player_number):
                    self.send_reply_to_client(command, player)


    def lobby_join(self, client_address, room_number, create_new_lobby=False):
        if create_new_lobby:
            self.room[room_number] = []  # We create a new lobby

        # There cannot be more than 4 players and no less than 2 players in a lobby
        if len(self.room[room_number]) >= 4:
            self.send_reply_to_client("lobbyjoin_failed", client_address)
            return

        self.room[room_number].append(client_address)
        self.send_reply_to_client(f"lobbyjoin_success_{len(self.room[room_number])}", client_address)

    def send_reply_to_client(self, response, client_address):
        self.server_socket.sendto(response.encode('utf-8'), client_address)


if __name__ == '__main__':
    server = Server()
    server.listen()
