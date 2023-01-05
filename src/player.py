import pygame


class Player:

    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 0, 0)
        self.walk_images = [pygame.image.load(f"../assets/player/player_walk_{i}.png") for i in range(4)]
        self.__animation_delay = 60
        self.__animation_index = 0
        self.animation_counter = 0
        self.moving_right = False
        self.moving_left = False
        self.name = name
        self.mask = pygame.mask.from_surface(self.walk_images[0])

    def draw(self, display):
        if self.__animation_index > 3:
            self.__animation_index = 0

        img = self.walk_images[self.__animation_index]

        img = pygame.transform.scale(img, (self.width, self.height))
        if self.moving_left:
            img = pygame.transform.flip(img, flip_x=True, flip_y=False)
        display.blit(img, (self.x, self.y))

        self.animation_counter += 1
        if self.animation_counter > self.__animation_delay:
            self.__animation_index += 1
            self.animation_counter = 0
