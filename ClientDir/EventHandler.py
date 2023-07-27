import pygame
from pygame.locals import *
import DrawnThingsTracker
import GlobalVariables
from Pen import Pen
from TextWriter import Writer
from DrawObject import DrawObject
from WordDisplay.DisplayDrawer import DisplayDrawer


class EventHandler:
    def __init__(self, screen, client):
        self.screen = screen
        self.pen = Pen(screen)
        self.client = client
        self.writer = Writer(self.screen, client)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GlobalVariables.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pen.isPressed = True

            if event.type == pygame.MOUSEBUTTONUP:
                self.pen.isPressed = False

            if event.type == pygame.MOUSEMOTION and self.pen.isPressed:
                if self.pen.isTurnToDraw:

                    (x, y) = pygame.mouse.get_pos()

                    if x >= 700:
                        return

                    self.pen.draw(x, y)
                    DrawnThingsTracker.draw_coordinates.append(DrawObject(x, y, self.pen.drawSize, self.pen.BLUE))

                    pygame.display.flip()

            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.writer.backspace()

                elif event.key == K_RETURN:
                    self.writer.enter()

                else:
                    self.writer.write(event.unicode)
