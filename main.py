import pygame
from Pen import Pen
import GlobalVariables
from EventHandler import EventHandler
from BoardDraw import Board

pygame.init()

# Sets up the scene
screen = pygame.display.set_mode((1000, 600))
BGCOLOR = (255, 255, 255)
screen.fill(BGCOLOR)

# Draws the board
board = Board(screen)
board.draw_stage()

pygame.display.flip()

# Sets up variables
pen = Pen(screen)
is_pressed = False
running = True
is_turn_to_draw = True
event_handler = EventHandler(screen)

while GlobalVariables.running:
    event_handler.handle_events()


exit()
