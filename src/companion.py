import pygame
from typing import Union
import random

class Companion:

    def __init__(self, display, x, y, animation_images, shot_sound, cool_down_timer=60):

        # args
        self.display = display
        self.x = x
        self.y = y
        self.animation_images = animation_images
        self.shot_sound = shot_sound

        # handle what sprite is show and how
        self.__animation_delay = 60
        self.__animation_index = 0
        self.__animation_counter = 0
        self.flip = False

        self.alive = True
        self.speed = 1
        self.kills = 0

        # handel shooting
        self.uses_projectiles = True
        self.__cool_down_timer = cool_down_timer
        self.__cool_down_timer_index = random.randint(0, self.__cool_down_timer)

    def __select_draw_image(self):
        if self.__animation_counter > self.__animation_delay:
            self.__animation_index += 1
            self.__animation_counter = 0
        if self.__animation_index >= len(self.animation_images):
            self.__animation_index = 0

    def draw(self, display_scroll_x, display_scroll_y):
        self.__select_draw_image()
        img = self.animation_images[self.__animation_index]
        img = pygame.transform.flip(img, flip_x=self.flip, flip_y=False)
        self.display.blit(img, (self.x - display_scroll_x, self.y - display_scroll_y))

    def fire_projectile(self) -> bool:
        if not self.uses_projectiles:
            return False
        if self.__cool_down_timer_index == 0:
            self.__cool_down_timer_index = self.__cool_down_timer
            return True
        self.__cool_down_timer_index -= 1
        return False
