import pygame


class TileSheet:

    def __init__(self, image, tile_size, n_rows, n_columns, scale: tuple[int, int] = None):
        self.image = image
        self.tile_size = tile_size
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.scale = scale
        self.tile_table = self.get_tile_table()

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




