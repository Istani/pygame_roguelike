import pygame.draw
import math


class Projectile:

    def __init__(self, x_mouse, y_mouse, player, animation_images, color=(255, 0, 0), speed=15, dev_view=True):
        self.x = int(player.x)
        self.y = int(player.y)
        self.x_mouse = x_mouse
        self.y_mouse = y_mouse
        self.color = color
        self.speed = speed
        self.angle = math.atan2(self.y - y_mouse, self.x  - x_mouse)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.alive = True
        self.animation_images = animation_images
        self.__animation_delay = 30
        self.rect = self.animation_images[0].get_rect()
        self.mask = pygame.mask.from_surface(self.animation_images[0])
        self.__animation_index = 0
        self.animation_counter = 0
        self.player = player
        self.display = player.display
        self.dev_view = dev_view

    def draw(self):
        if not self.alive:
            return
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        if self.__animation_index >= len(self.animation_images):
            self.__animation_index = 0
        self.rect.x = self.x
        self.rect.y = self.y
        if self.dev_view:
            pygame.draw.rect(self.display, (0, 0, 255), self.rect)
        self.display.blit(self.animation_images[self.__animation_index], (self.x, self.y))
        self.animation_counter += 1
        if self.animation_counter > self.__animation_delay:
            self.__animation_index += 1
            self.animation_counter = 0


