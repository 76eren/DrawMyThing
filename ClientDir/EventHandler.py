import pygame
from pygame.locals import *
import DrawnThingsTracker
import GlobalVariables
from Pen import Pen
from TextWriter import Writer
from DrawObject import DrawObject
from BoardDraw import Board


class EventHandler:
    def __init__(self, screen, client):
        self.screen = screen

        # Sometimes I feel like making all of these objects a static somewhere would have saved me a lot of trouble
        self.client = client
        self.pen = Pen(screen)
        self.writer = Writer(self.screen, client)
        self.board = Board(self.screen)

        self.board.redraw_all()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GlobalVariables.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pen.isPressed = True

            if event.type == pygame.MOUSEBUTTONUP:
                self.pen.isPressed = False

            if event.type == pygame.MOUSEMOTION and self.pen.isPressed:
                if self.client.turn_to_draw:

                    (x, y) = pygame.mouse.get_pos()

                    if x >= 700:
                        return

                    self.pen.draw(x, y)
                    DrawnThingsTracker.StaticDrawnThings.draw_coordinates.append(
                        DrawObject(x, y, self.pen.drawSize, self.pen.BLUE))

                    self.client.send_message(f"coordinate_{self.client.player_number}_{self.client.lobby_number}_{x}_{y}")

                    pygame.display.flip()

            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.writer.backspace()

                elif event.key == K_RETURN:
                    self.writer.enter()

                else:
                    self.writer.write(event.unicode)

    def check_if_anything_needs_to_be_displayed(self):
        pass
