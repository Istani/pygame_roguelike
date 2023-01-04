import pygame
import random


class Slime:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animation_images = [pygame.image.load(f"../assets/slime/slime_animation_{i}.png") for i in range(4)]
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-300, 300)
        self.offset_y = random.randrange(-300, 300)

    def draw(self, display, display_scroll, player):
        if self.animation_count + 1 == 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.reset_offset == 0:
            self.offset_x = random.randrange(-300, 300)
            self.offset_y = random.randrange(-300, 300)
            self.reset_offset = random.randrange(120, 150)
        else:
            self.reset_offset -= 1

        if player.x + self.offset_x > self.x - display_scroll[0]:
            self.x += 1
        elif player.x + self.offset_x < self.x - display_scroll[0]:
            self.x -= 1

        if player.y + self.offset_y > self.y - display_scroll[1]:
            self.y += 1
        elif player.y + self.offset_y < self.y - display_scroll[1]:
            self.y -= 1

        display.blit(pygame.transform.scale(self.animation_images[self.animation_count // 4], (32, 30)),
                     (self.x - display_scroll[0], self.y - display_scroll[1]))
