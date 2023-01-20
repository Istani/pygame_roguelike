import pygame


class Companion:

    def __init__(self, display, x, y, animation_images):

        # args
        self.display = display
        self.x = x
        self.y = y
        self.animation_images = animation_images

        # handle what sprite is show and how
        self.__animation_delay = 60
        self.__animation_index = 0
        self.__animation_counter = 0
        self.flip = False

        self.alive = True
        self.speed = 1

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
