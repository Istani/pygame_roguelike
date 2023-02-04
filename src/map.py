from perlin_noise import PerlinNoise
import random
import pygame


class Map:

    def __init__(self, tile_table, tile_size=32, scale=3, random_sprites=False):
        self.tile_table = tile_table
        self.tile_size = tile_size
        self.scale = scale
        self.screen_width = pygame.display.get_window_size()[0]
        self.screen_height = pygame.display.get_window_size()[1]
        self.screen_rows = int(self.screen_width / self.tile_size)
        self.screen_columns = int(self.screen_height / self.tile_size)
        self.n_row = self.screen_rows * self.scale
        self.n_cols = self.screen_columns * self.scale
        self.noise = PerlinNoise(octaves=6, seed=random.randint(0, 100000))
        self.place = [[self.noise([i / self.n_row, j / self.n_cols]) for j in range(self.n_cols)] for i in
                      range(self.n_row)]

        self.random_sprites = random_sprites
        self.grass_tile_row = None
        self.grass_tile_column = None
        self.objects = None
        self.select_map_tiles()
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
                    tile_row, tile_column = self.grass_tile_row, self.grass_tile_column
                self.object_draw.append(
                    (self.tile_table[tile_row][tile_column], (x * self.tile_size, y * self.tile_size)))

    def select_map_tiles(self):
        n_tiles = 5
        if self.random_sprites:
            self.select_random_tiles(n_tiles)
        else:
            self.grass_tile_row, self.grass_tile_column = 2, 7
            l = [(20, 11), (21, 11), (17, 11),(11, 11), (None, None)]
            self.objects = l[::-1]

    def select_random_tiles(self, n_random_objects):
        self.grass_tile_row = random.randint(0, 9)
        self.grass_tile_column = random.randint(0, 10)
        self.objects = []
        for _ in range(n_random_objects):
            r = random.randint(11, 13)
            c = random.randint(0, 24)
            if r == 11:
                c = random.randint(10, 24)
            self.objects.append((c, r))

    def draw(self, screen, display_scroll_x, display_scroll_y):
        for obj in self.object_draw:
            x = obj[1][0] - display_scroll_x - self.screen_rows * self.tile_size
            y = obj[1][1] - display_scroll_y - self.screen_columns * self.tile_size

            if -50 < x < self.screen_width and -50 < y < self.screen_height:
                screen.blit(self.tile_table[self.grass_tile_row][self.grass_tile_column], (x, y))
                screen.blit(obj[0], (x, y))
