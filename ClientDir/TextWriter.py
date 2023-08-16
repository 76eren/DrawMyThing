import pygame
from BoardDraw import Board
from TextObject import TextObject
import DrawnThingsTracker

pygame.init()
pygame.font.init()


class Writer:
    def __init__(self, screen, client):
        self.font = pygame.font.SysFont('calibri', 25)
        self.font2 = pygame.font.SysFont('calibri', 20)

        self.screen = screen
        self.board = Board(self.screen)

        self.text_coords = (720, 515)
        self.client = client

    def write(self, key):
        # Blocks underscores in the chat, so it won't interfere with the client server communication
        if key == "_":
            return

        DrawnThingsTracker.StaticDrawnThings.text += key
        DrawnThingsTracker.StaticDrawnThings.typed_message = DrawnThingsTracker.StaticDrawnThings.text

        self.board.redraw_all()

    def backspace(self):
        self.board.redraw_all()

        if DrawnThingsTracker.StaticDrawnThings.text != "":
            DrawnThingsTracker.StaticDrawnThings.text = DrawnThingsTracker.StaticDrawnThings.text[:-1]

            self.board.redraw_all()
            DrawnThingsTracker.StaticDrawnThings.typed_message = DrawnThingsTracker.StaticDrawnThings.text

    def enter(self):
        if DrawnThingsTracker.StaticDrawnThings.text == "":
            return

        if DrawnThingsTracker.StaticDrawnThings.text.startswith("/connect") and not self.client.is_connected:
            self.client.outgoing_command(DrawnThingsTracker.StaticDrawnThings.text)
            DrawnThingsTracker.StaticDrawnThings.chat_history.append(TextObject("Attempting to connect", "SYSTEM"))
        else:
            DrawnThingsTracker.StaticDrawnThings.chat_history.append(
                TextObject(DrawnThingsTracker.StaticDrawnThings.text, f"User {self.client.player_number}"))
            self.check_for_possible_commands()

        DrawnThingsTracker.StaticDrawnThings.text = ""
        DrawnThingsTracker.StaticDrawnThings.typed_message = DrawnThingsTracker.StaticDrawnThings.text

        self.board.redraw_all()

    def check_for_possible_commands(self):
        # TODO: A LOT OF THESE BELONG IN THE ClientDir.command function, the string that should be sent to the server
        #  should be formatted there, NOT HERE

        if self.client.is_connected:
            # Format: sendChatMessage_playernumber_lobbynumber_message
            self.client.outgoing_command(
                f"sendChatMessage_{self.client.player_number}_{self.client.lobby_number}_{DrawnThingsTracker.StaticDrawnThings.text}")

            # Format: startGame_playernumber_lobbynumber
            if DrawnThingsTracker.StaticDrawnThings.text.startswith("/startgame"):
                self.client.outgoing_command(f"startGame_{self.client.player_number}_{self.client.lobby_number}")

    def update_chat(self):
        self.board.redraw_all()

    def push_a_message_to_chat(self, message, user):
        DrawnThingsTracker.StaticDrawnThings.chat_history.append(TextObject(message, user))
        self.update_chat()
