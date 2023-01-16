from perlin_noise import PerlinNoise
import random
import numpy as np
import pygame


def select_random_tiles(n_random_objects=5):
    objects = []
    for _ in range(n_random_objects):
        r = random.randint(11, 13)
        c = random.randint(0, 24)
        if r == 11:
            c = random.randint(10, 24)
        objects.append((c, r))
    return objects


class Map:

    def __init__(self, tile_table, tile_size=32, scale=3):
        self.tile_table = tile_table
        self.tile_size = tile_size
        self.scale = scale
        self.screen_rows = int(pygame.display.get_window_size()[0] / self.tile_size)
        self.screen_columns = int(pygame.display.get_window_size()[1] / self.tile_size)
        self.n_row = self.screen_rows * self.scale
        self.n_cols = self.screen_columns * self.scale
        self.noise = PerlinNoise(octaves=6, seed=random.randint(0, 100000))
        self.place = [[self.noise([i / self.n_row, j / self.n_cols]) for j in range(self.n_cols)] for i in
                      range(self.n_row)]

        self.grass_tile_row = random.randint(0, 9)
        self.grass_tile_column = random.randint(0, 10)

        self.objects = select_random_tiles(5)
        self.__init_map()

    def __init_map(self):
        self.object_draw = []
        for x in range(self.n_row):
            for y in range(self.n_cols):
                if self.place[x][y] >= 0.7:
                    tile_row, tile_column = self.objects[0]
                elif self.place[x][y] >= 0.3:
                    tile_row, tile_column = self.objects[1]
                elif self.place[x][y] >= 0.1:
                    tile_row, tile_column = self.objects[2]
                elif self.place[x][y] >= 0.01:
                    tile_row, tile_column = self.objects[3]
                elif self.place[x][y] >= -0.001:
                    tile_row, tile_column = self.objects[4]
                else:
                    tile_row, tile_column = self.objects[0]
                self.object_draw.append(
                    (self.tile_table[tile_row][tile_column], (x * self.tile_size, y * self.tile_size)))

    def draw(self, screen, display_scroll_x, display_scroll_y):
        for obj in self.object_draw:
            x = obj[1][0] - display_scroll_x - self.screen_rows * self.tile_size
            y = obj[1][1] - display_scroll_y - self.screen_columns * self.tile_size
            screen.blit(self.tile_table[self.grass_tile_row][self.grass_tile_column], (x, y))
            screen.blit(obj[0], (x, y))


if __name__ == '__main__':
    map = Map()

    print(map.place.shape)
