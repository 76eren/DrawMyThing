import pygame
from BoardDraw import Board
pygame.init()
pygame.font.init()


class Writer:
    def __init__(self, screen):
        self.text = ""
        self.chat = []
        self.font = pygame.font.SysFont('calibri', 15)
        self.screen = screen
        self.board = Board(self.screen)

    def write(self, key):
        self.text += key

        text_surface = self.font.render(self.text, False, (0, 0, 255))
        self.screen.blit(text_surface, (50, 50))
        pygame.display.flip()

    def backspace(self):
        self.screen.fill((255, 255, 255))
        self.board.draw_stage()
        self.board.draw_all_of_the_rest()

        if self.text != "":
            self.text = self.text[:-1]

            text_surface = self.font.render(self.text, False, (0, 0, 255))
            self.screen.blit(text_surface, (50, 50))
            pygame.display.flip()

    def enter(self):
        print(self.text)
        self.text = ""

    def update_chat(self):
        self.chat.append(self.text)
        self.text = ""
