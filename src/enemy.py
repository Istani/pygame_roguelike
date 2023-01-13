import pygame
import random
from src.projectile import EnemyProjectile
from src.ai import AI
from typing import Union


class Enemy:

    def __init__(self, display, enemy_images, hit_sound, ai: AI, display_scroll_x: int, display_scroll_y: int, speed=1,
                 dev_view=False, live_max=100, uses_projectiles=False, cool_down_timer=120):
        self.x = None
        self.y = None
        self.animation_images = enemy_images
        self.mask = pygame.mask.from_surface(self.animation_images[0])
        self.rect = self.animation_images[0].get_rect()
        self.animation_timer = 16
        self.timer_index = 0
        self.animation_index = 0
        self.display = display
        self.alive = True
        self.live_max = live_max
        self.live = live_max
        self.hit_sound = hit_sound
        self.ai = ai
        self.flip = False
        self.w, self.h = pygame.display.get_surface().get_size()
        self.out_of_screen_offset = 10
        self.speed = speed
        self.spawn(display_scroll_x, display_scroll_y)
        self.dev_view = dev_view
        self.live_font = pygame.font.SysFont("comicsans", 15)
        self.dev_font = pygame.font.SysFont("comicsans", 18)
        self.knock_back_velocity_x = None
        self.knock_back_velocity_y = None
        self.knock_back_timer = 0
        self.cool_down_timer = cool_down_timer
        self.cool_down_timer_index = random.randint(0, self.cool_down_timer)
        self.uses_projectiles = uses_projectiles
        self.live_bar_scale = 0.3

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

    def draw_health_bar(self, display_scroll_x, display_scroll_y):
        position = (self.x - display_scroll_x, self.y - display_scroll_y - 10)
        rect_red = (position, (self.live_max * self.live_bar_scale, 5))
        rect_green = (position, (self.live * self.live_bar_scale, 5))
        pygame.draw.rect(self.display, (255, 0, 0), rect_red)
        pygame.draw.rect(self.display, (0, 255, 0), rect_green)

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
        if self.dev_view:
            live = self.live_font.render(str(self.live) + " /" + str(self.live_max), True, (255, 255, 255))
            self.display.blit(live, (self.x - 15 - display_scroll_x, self.y - 18 - display_scroll_y))
            pos = (self.x - display_scroll_x, self.y - display_scroll_y)
            dev_pos = self.dev_font.render(str(pos), True, (255, 255, 255))
            self.display.blit(dev_pos, (self.x - display_scroll_x - 50, self.y - display_scroll_y - 50))
            pygame.draw.rect(self.display, (255, 0, 0), self.rect)
        self.display.blit(img, (self.x - display_scroll_x, self.y - display_scroll_y))
        self.draw_health_bar(display_scroll_x, display_scroll_y)

    def fire_projectile(self, player, animation_images) -> Union[EnemyProjectile, None]:
        if not self.uses_projectiles:
            return
        if self.cool_down_timer_index == 0:
            self.cool_down_timer_index = self.cool_down_timer
            return EnemyProjectile(monster=self, player=player, animation_images=animation_images,
                                   dev_view=self.dev_view)
        self.cool_down_timer_index -= 1
