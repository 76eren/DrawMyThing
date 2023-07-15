import pygame


pygame.init()


class Pen:
    def __init__(self, screen):
        self.screen = screen
        self.BLUE = (0, 0, 255)  # THIS IS HARDCODED AND NEEDS TO CHANGE LATER ON
        self.drawSize = 5

        self.isTurnToDraw = True
        self.isPressed = False

    def draw(self, x, y):
        pygame.draw.circle(self.screen, self.BLUE, (x, y), self.drawSize)
