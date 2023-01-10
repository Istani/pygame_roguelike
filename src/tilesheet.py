import random

import pygame


class TileSheet:

    def __init__(self, image, tile_size, n_rows, n_columns, scale: tuple[int, int] = None):
        self.image = image
        self.tile_size = tile_size
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.scale = scale
        self.tile_table = self.get_tile_table()

        # random grass
        self.grass_tile_row = random.randint(0, 9)
        self.grass_tile_column = random.randint(0, 10)

        self.n_random_objects = 5
        self.objects = []
        # 5 random sprites for the env
        for _ in range(self.n_random_objects):
            r = random.randint(11, 13)
            if r == 11:
                c = random.randint(10, 24)
            else:
                c = random.randint(0, 24)
            self.objects.append((c, r))
        self.object_draw = None


    def get_tile_table(self):
        tile_table = []
        for x in range(self.n_columns):
            row = []
            for y in range(self.n_rows):
                rectangle = (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                tile = self.image.subsurface(rectangle)
                if self.scale is not None:
                    tile = pygame.transform.scale(tile, self.scale)
                row.append(tile)
            tile_table.append(row)
        return tile_table

    def draw(self, screen, display_scroll_x, display_scroll_y):
        #  this function is just for development test and will be removed soon.
        s = 32
        n_row = int(pygame.display.get_window_size()[0] / s)
        n_cols = int(pygame.display.get_window_size()[1] / s)
        # draw all sprites
        for x in range(n_row):
            for y in range(n_cols):
                tile_x = x * s - display_scroll_x
                tile_y = y * s - display_scroll_y
                screen.blit(self.tile_table[self.grass_tile_row][self.grass_tile_column],
                            (tile_x, tile_y))

        if self.object_draw is None:
            self.object_draw = []
            for x in range(n_row):
                for y in range(n_cols):
                    if random.random() < 0.05:
                        tile_x = x * s - display_scroll_x
                        tile_y = y * s - display_scroll_y
                        tile_row, tile_column = self.objects[random.randint(0, self.n_random_objects - 2)]
                        print(tile_row, tile_column)
                        self.object_draw.append(
                            (self.tile_table[tile_row][tile_column], (tile_x, tile_y))
                        )
        else:
            for obj in self.object_draw:
                screen.blit(obj[0], (obj[1][0] - display_scroll_x , obj[1][1] - display_scroll_y))