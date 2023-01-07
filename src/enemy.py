import pygame


class Enemy:

    def __init__(self, x, y, display, enemy_images,hit_sound, ai):
        self.x = x
        self.y = y
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
        self.display.blit(img,(self.x - display_scroll_x, self.y - display_scroll_y))
        

