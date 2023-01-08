import pygame
import random


class Enemy:

    def __init__(self, display, enemy_images, hit_sound, ai, display_scroll_x, display_scroll_y, speed=1):
        self.x = None
        self.y = None
        self.animation_images = enemy_images
        self.mask = pygame.mask.from_surface(self.animation_images[0])
        self.animation_timer = 16
        self.timer_index = 0
        self.animation_index = 0
        self.display = display
        self.alive = True
        self.live = 100
        self.hit_sound = hit_sound
        self.ai = ai
        self.flip = False
        self.w, self.h = pygame.display.get_surface().get_size()
        self.out_of_screen_offset = 10
        self.speed = speed
        self.spawn(display_scroll_x, display_scroll_y)

    def spawn(self, display_scroll_x, display_scroll_y):
        self.x = display_scroll_x
        self.y = display_scroll_y
        rnd = random.randint(1, 4)
        if rnd == 1:
            self.x += random.randint(0, self.w)
            self.y += - self.out_of_screen_offset
        elif rnd == 2:
            self.x += random.randint(0, self.w)
            self.y += self.h + self.out_of_screen_offset
        elif rnd == 3:
            self.x += - self.out_of_screen_offset
            self.y += random.randint(0, self.h)
        else:
            self.y += random.randint(0, self.h)
            self.x += self.w + self.out_of_screen_offset

    def draw(self, display_scroll_x, display_scroll_y):
        if not self.alive:
            return
        if self.timer_index == self.animation_timer:
            self.animation_index += 1
            if self.animation_index >= len(self.animation_images):
                self.animation_index = 0
            self.timer_index = -1
        self.timer_index += 1
        img = self.animation_images[self.animation_index]
        img = pygame.transform.flip(img, flip_x=self.flip, flip_y=False)
        self.display.blit(img, (self.x - display_scroll_x, self.y - display_scroll_y))
