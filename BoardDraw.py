import pygame
import GlobalVariables
from Pen import Pen

pygame.init()

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.pen = Pen(self.screen)


    def draw_stage(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.line(self.screen, (0, 0, 0), (700, 0), (700, 600), 4)
        pygame.draw.line(self.screen, (0, 0, 0), (700, 500), (1000, 500), 4)

        pygame.display.flip()

    def draw_all_of_the_rest(self):
        for i in GlobalVariables.draw_coordinates:
            self.pen.draw(i.x, i.y)

