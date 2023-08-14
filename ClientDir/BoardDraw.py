import pygame
import DrawnThingsTracker
from Pen import Pen

pygame.init()


class Board:
    def __init__(self, screen, writer):
        self.screen = screen
        self.pen = Pen(self.screen)
        self.writer = writer

        self.font_for_current_written_text = pygame.font.SysFont('calibri', 25)
        self.font_for_display = pygame.font.SysFont('calibri', 55)
        self.font_for_chat = pygame.font.SysFont('calibri', 20)

        self.display_text_coordinates = (320, 10)
        self.current_written_text_coords = (720, 515)

    def redraw_all(self):
        self.screen.fill((255, 255, 255))
        self.draw_stage()
        self.draw_all_of_the_rest()

    def draw_stage(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.line(self.screen, (0, 0, 0), (700, 0), (700, 600), 4)
        pygame.draw.line(self.screen, (0, 0, 0), (700, 500), (1100, 500), 4)

        pygame.display.flip()

    def draw_all_of_the_rest(self):
        # We re-draw all the drawing made
        for i in DrawnThingsTracker.StaticDrawnThings.draw_coordinates:
            self.pen.draw(i.x, i.y)

        # Now we redraw the display, THIS DOES NOT WORK RIGHT NOW
        text_surface = self.font_for_display.render(DrawnThingsTracker.StaticDrawnThings.text_to_be_displayed, True,
                                                    (0, 0, 255))
        self.screen.blit(text_surface, self.display_text_coordinates)

        # Now we redraw the current written text
        text_surface = self.font_for_current_written_text.render(DrawnThingsTracker.StaticDrawnThings.text, True,
                                                                 (0, 0, 255))
        self.screen.blit(text_surface, self.current_written_text_coords)

        # This updates the chat
        amount_to_newline = 20
        current = 0
        # Now we re-draw the text on the chat
        for i in DrawnThingsTracker.StaticDrawnThings.chat_history:
            text = i.message
            user = i.sentByUser
            message = f"{user}> {text}"

            text_surface = self.font_for_chat.render(message, False, (0, 0, 0))
            self.screen.blit(text_surface, (720, current))

            current += amount_to_newline

        pygame.display.flip()

