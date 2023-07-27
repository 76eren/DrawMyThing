import pygame
import pygame.display
from ClientDir import BoardDraw


class Display:
    def __init__(self, screen, client):
        self.font = pygame.font.SysFont('calibri', 25)
        self.screen = screen
        self.board = None # TODO: URGENT A reference to this still must be made somehow for the other functions to work

        self.text_coordinates = (100, 100)
        self.client = client

    def update_field(self, text):
        self.board.redraw_all()
        text_surface = self.font.render(text, True, (0, 0, 255))
        self.screen.blit(text_surface, self.text_coordinates)
        pygame.display.flip()

