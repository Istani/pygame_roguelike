import random


class Item:

    def __init__(self, display, image, x, y):
        self.display = display
        self.image = image
        self.x = x
        self.y = y
        self.alive = True
        self.rect = self.image.get_rect()
        self.increase_live_points_by = 10

    def draw(self, display_scroll_x, display_scroll_y):
        self.display.blit(self.image, (self.x - display_scroll_x, self.y - display_scroll_y))


class Loot:

    def __init__(self, assets):
        self.assets = assets

    def drop_foot(self, display, x, y):
        img = self.assets.food_images[random.randint(0, len(self.assets.food_images) - 1)]
        return Item(display, img, x, y)
