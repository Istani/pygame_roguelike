import pygame.draw
import math


class Projectile:

    def __init__(self, x_mouse, y_mouse, player, animation_images, damage=50, speed=15,
                 knock_back_duration=15, dev_view=False):
        self.x = int(player.x)
        self.y = int(player.y)
        self.x_mouse = x_mouse
        self.y_mouse = y_mouse
        self.speed = speed
        self.angle = math.atan2(self.y - y_mouse, self.x - x_mouse)
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
        self.damage = damage
        self.knock_back_duration = knock_back_duration

    def draw(self, display_scroll_x=0, display_scroll_y=0):
        if not self.alive:
            return
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        if self.__animation_index >= len(self.animation_images):
            self.__animation_index = 0
        self.rect.x = self.x - display_scroll_x
        self.rect.y = self.y - display_scroll_y
        if self.dev_view:
            pygame.draw.rect(self.display, (0, 0, 255), self.rect)
        self.display.blit(self.animation_images[self.__animation_index],
                          (self.x - display_scroll_x, self.y - display_scroll_y))
        self.animation_counter += 1
        if self.animation_counter > self.__animation_delay:
            self.__animation_index += 1
            self.animation_counter = 0


class EnemyProjectile(Projectile):

    def __init__(self, monster, player, animation_images, cool_down_timer=35, damage=10, speed=5, knock_back_duration=3,
                 dev_view=False):
        self.cool_down_timer = cool_down_timer
        self.cool_down_timer_index = 0
        x = player.x + player.display_scroll_x
        y = player.y + player.display_scroll_y
        super().__init__(x_mouse=x, y_mouse=y, player=monster, animation_images=animation_images,
                         damage=damage, speed=speed, knock_back_duration=knock_back_duration, dev_view=dev_view)
