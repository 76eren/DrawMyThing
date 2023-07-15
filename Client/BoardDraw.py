import pygame
import DrawnThingsTracker
from Pen import Pen

pygame.init()


class Board:
    def __init__(self, screen, writer):
        self.screen = screen
        self.pen = Pen(self.screen)
        self.writer = writer


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
        for i in DrawnThingsTracker.draw_coordinates:
            self.pen.draw(i.x, i.y)

        # We re-draw all the chat
        self.writer.update_chat()


    # This function is supposed to be called from the TextWriter.update_chat function
    # The reason I made this function is to prevent recursion
    def draw_some_of_the_rest(self):
        # We re-draw all the drawing made
        for i in DrawnThingsTracker.draw_coordinates:
            self.pen.draw(i.x, i.y)





