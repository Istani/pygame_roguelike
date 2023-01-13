import pygame


class Player:

    def __init__(self, x, y, name, player_images, display, max_live=100):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.walk_images = player_images
        self.__animation_delay = 60
        self.__animation_index = 0
        self.animation_counter = 0
        self.moving_right = False
        self.moving_left = False
        self.name = name
        self.mask = pygame.mask.from_surface(self.walk_images[0])
        self.rect = self.walk_images[0].get_rect()
        self.kills = 0
        self.max_live = max_live
        self.live = max_live
        self.alive = True
        self.display_scroll_x = 0
        self.display_scroll_y = 0
        self.display = display
        self.live_bar_scale = 0.5

    def move(self, keys):
        if keys[pygame.K_a]:
            self.display_scroll_x -= 5
            self.animation_counter += 10
            self.moving_left = True
            self.moving_right = False
        if keys[pygame.K_d]:
            self.display_scroll_x += 5
            self.animation_counter += 10
            self.moving_right = True
            self.moving_left = False
        if keys[pygame.K_w]:
            self.display_scroll_y -= 5
        if keys[pygame.K_s]:
            self.display_scroll_y += 5

    def draw_health_bar(self):
        rect_red = ((self.x, self.y - 25), (self.max_live * self.live_bar_scale, 10))
        rect_green = ((self.x, self.y - 25), (self.live * self.live_bar_scale, 10))
        pygame.draw.rect(self.display, (255, 0, 0), rect_red)
        pygame.draw.rect(self.display, (0, 255, 0), rect_green)

    def draw(self):
        if not self.alive:
            return
        if self.live <= 0:
            self.alive = False
        if self.__animation_index > 3:
            self.__animation_index = 0
        img = self.walk_images[self.__animation_index]
        if self.moving_left:
            img = pygame.transform.flip(img, flip_x=True, flip_y=False)
        self.display.blit(img, (self.x, self.y))
        self.animation_counter += 1
        if self.animation_counter > self.__animation_delay:
            self.__animation_index += 1
            self.animation_counter = 0
        self.draw_health_bar()
