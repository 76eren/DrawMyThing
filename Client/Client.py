import socket
import threading


class Client:
    def __init__(self):
        self.server_ip = '127.0.0.1'
        self.server_port = 6969
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.bind(('0.0.0.0', 0))  # Bind to any available local address and port
        self.player_number = ""
        self.event_handler = None  # Woohoo, nested object hell. Boy I sure love OOP
        self.is_connected = False
        self.lobby_number = None

        # Starts the message listener in another thread
        message_listener = threading.Thread(target=self.receive_message)

        message_listener.start()

    def assign_event_handler(self, event_handler):
        self.event_handler = event_handler

    def send_message(self, message):
        self.client_socket.sendto(message.encode('utf-8'), (self.server_ip, self.server_port))
        print("Sent message to server: {}".format(message))

    # Has to be run from a separate thread
    def receive_message(self):
        while True:
            response, server_address = self.client_socket.recvfrom(1024)
            response = response.decode('utf-8')
            self.command(response)
            print(f"Received response from server: {response}")

    # TODO: Make different functions for incoming and outgoing commands
    def command(self, command: str):
        print(f"Command is: {command}")
        if command.startswith("/connect"):
            try:
                room_to_join = command.split(" ")[1]
                self.lobby_number = room_to_join
                self.send_message(f"connectroom_{room_to_join}")


            except IndexError:
                print("Invalid command")
                return

        # This means the client successfully joined a lobby or was unable to join a lobby
        if command.startswith("lobbyjoin_"):
            if "lobbyjoin_failed" in command:
                print("Failed to join lobby")
                self.send_message_to_chat("Failed to join lobby", "SYSTEM")
                self.lobby_number = None
                return

            if "lobbyjoin_success" in command:
                self.assign_player_number(command.split("_")[2])
                print(f"Successfully joined lobby, you are player {self.player_number}")
                self.send_message_to_chat(f"Successfully joined lobby", "SYSTEM")
                self.send_message_to_chat(f"you are player {self.player_number}", "SYSTEM")
                self.is_connected = True


        # Receives chat message from server
        # Format: ChatMessage_playernumber_lobbynumber_message
        if command.startswith("ChatMessage"):
            player_number = command.split("_")[1]
            message = command.split("_")[3]
            self.send_message_to_chat(message, f"User {player_number}")

        # Sends chat message to server
        # Format: sendChatMessage_playernumber_lobbynumber_message
        if command.startswith("sendChatMessage"):
            command = command.replace("send", "")
            self.send_message(command)

    def assign_player_number(self, number):
        self.player_number = number

    def send_message_to_chat(self, message, user):
        self.event_handler.writer.push_a_message_to_chat(message, user)
