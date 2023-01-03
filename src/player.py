import pygame.draw


class Player:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 0, 0)

    def draw(self, display):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))
