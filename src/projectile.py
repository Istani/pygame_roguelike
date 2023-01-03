import pygame.draw
import math

class Projectile:

    def __init__(self, x, y, x_mouse, y_mouse, color=(255, 0, 0), speed=15, size=5):
        self.x = x
        self.y = y
        self.x_mouse = x_mouse
        self.y_mouse = y_mouse
        self.color = color
        self.speed = speed
        self.size = size
        self.angle = math.atan2(y-y_mouse, x - x_mouse)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    def draw(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        pygame.draw.circle(display, self.color, (self.x, self.y), self.size)
