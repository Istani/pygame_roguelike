import pygame.draw
import math


class Projectile:

    def __init__(self, x, y, x_mouse, y_mouse,  color=(255, 0, 0), speed=15, size=5):
        self.x = x
        self.y = y
        self.x_mouse = x_mouse
        self.y_mouse = y_mouse
        self.color = color
        self.speed = speed
        self.size = size
        self.angle = math.atan2(y - y_mouse, x - x_mouse)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.alive = True
        self.animation_images = [pygame.image.load(f"../assets/projectiles/fire_bullet_{i}.png") for i in range(1, 4)]
        self.animation_images = [pygame.transform.scale(i, (self.size, self.size)) for i in self.animation_images]
        self.__animation_delay = 30

        self.mask = pygame.mask.from_surface(self.animation_images[0])
        self.__animation_index = 0
        self.animation_counter = 0

    def draw(self, display, enemies):
        if not self.alive:
            return
        #for e in enemies:
        #    offset_x = self.x - e.x
        #    offset_y = self.y - e.y
        #    if e.mask.overlap(self.mask, (offset_x, offset_y)) is not None:
        #        self.alive = False
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        if self.__animation_index >= len(self.animation_images):
            self.__animation_index = 0
        display.blit(self.animation_images[self.__animation_index], (self.x, self.y))
        self.animation_counter += 1
        if self.animation_counter > self.__animation_delay:
            self.__animation_index += 1
            self.animation_counter = 0