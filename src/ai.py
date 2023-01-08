import random


class AI:

    def __init__(self):
        self.offset_min = -300
        self.move_offset_max = 300
        self.reset_counter_min = 120
        self.reset_counter_max = 150
        self.offset_x = None
        self.offset_y = None
        self.reset_counter = None
        self.reset()

    def reset(self):
        self.offset_x = random.randrange(self.offset_min, self.move_offset_max)
        self.offset_y = random.randrange(self.offset_min, self.move_offset_max)
        self.reset_counter = random.randrange(self.reset_counter_min, self.reset_counter_max)

    def move_enemy(self, player, enemy):
        self.reset_counter -= 1
        if self.reset_counter == 0:
            self.reset()
        if player.x + self.offset_x > enemy.x - player.display_scroll_x:
            enemy.x += enemy.speed
            enemy.flip = False
        elif player.x + self.offset_x < enemy.x - player.display_scroll_x:
            enemy.x -= enemy.speed
            enemy.flip = True

        if player.y + self.offset_y > enemy.y - player.display_scroll_y:
            enemy.y += enemy.speed
        elif player.y + self.offset_y < enemy.y - player.display_scroll_y:
            enemy.y -= enemy.speed
