import pygame
from BoardDraw import Board
from TextObject import TextObject

pygame.init()
pygame.font.init()


class Writer:
    def __init__(self, screen, client):
        self.text = ""
        self.font = pygame.font.SysFont('calibri', 25)
        self.font2 = pygame.font.SysFont('calibri', 20)

        self.screen = screen
        self.board = Board(self.screen, self)
        self.chat_history = []  # Keeps track of all the chat messages
        self.typed_message = ""  # Keeps track of the message the user is typing

        self.text_coords = (720, 515)
        self.client = client

    def write(self, key):
        self.text += key
        self.typed_message = self.text

        text_surface = self.font.render(self.text, True, (0, 0, 255))
        self.screen.blit(text_surface, self.text_coords)
        pygame.display.flip()

    def backspace(self):
        self.screen.fill((255, 255, 255))
        self.board.draw_stage()
        self.board.draw_all_of_the_rest()

        if self.text != "":
            self.text = self.text[:-1]

            text_surface = self.font.render(self.text, True, (0, 0, 255))
            self.screen.blit(text_surface, self.text_coords)
            pygame.display.flip()
            self.typed_message = self.text

    def enter(self):
        if self.text == "":
            return

        self.board.redraw_all()

        if self.text.startswith("/connect"):
            self.client.command(self.text)
            self.chat_history.append(TextObject("Attempting to connect", "SYSTEM"))
        else:
            self.chat_history.append(TextObject(self.text, "User 1"))

        self.text = ""
        self.typed_message = self.text
        self.update_chat()

        self.board.redraw_all()

        text_surface = self.font.render(self.text, False, (0, 0, 255))
        self.screen.blit(text_surface, self.text_coords)

    def update_chat(self):
        self.screen.fill((255, 255, 255))
        self.board.draw_stage()
        self.board.draw_some_of_the_rest()

        amount_to_newline = 20
        current = 0
        # Now we re-draw the text on the chat
        for i in self.chat_history:
            text = i.message
            user = i.sentByUser
            message = f"{user}> {text}"

            text_surface = self.font2.render(message, False, (0, 0, 0))
            self.screen.blit(text_surface, (720, current))
            pygame.display.flip()

            current += amount_to_newline

    def push_a_message_to_chat(self, message, user):
        self.chat_history.append(TextObject(message, user))
        self.update_chat()
