import random


class AI:

    def __init__(self, ai_type=1):
        self.offset_min = -300
        self.move_offset_max = 300
        self.reset_counter_min = 120
        self.reset_counter_max = 150
        self.offset_x = None
        self.offset_y = None
        self.reset_counter = None
        self.reset()
        self.ai_type = ai_type

    def reset(self):
        self.offset_x = random.randrange(self.offset_min, self.move_offset_max)
        self.offset_y = random.randrange(self.offset_min, self.move_offset_max)
        self.reset_counter = random.randrange(self.reset_counter_min, self.reset_counter_max)

    def move_enemy_default(self, player, enemy):
        self.reset_counter -= 1
        if self.reset_counter == 0:
            self.reset()
        if player.x + self.offset_x > enemy.x - player.display_scroll_x:
            enemy.x = enemy.x + enemy.speed
            enemy.flip = False
        elif player.x + self.offset_x < enemy.x - player.display_scroll_x:
            enemy.x = enemy.x - enemy.speed
            enemy.flip = True
        if player.y + self.offset_y > enemy.y - player.display_scroll_y:
            enemy.y = enemy.y + enemy.speed
        elif player.y + self.offset_y < enemy.y - player.display_scroll_y:
            enemy.y = enemy.y - enemy.speed

    @staticmethod
    def move_enemy_aggressive(player, enemy):
        ex, ey = enemy.x - player.display_scroll_x, enemy.y - player.display_scroll_y
        if ex < player.x:
            enemy.x = enemy.x + enemy.speed
            enemy.flip = False
        elif ex > player.x:
            enemy.x = enemy.x - enemy.speed
            enemy.flip = True
        if ey < player.y:
            enemy.y = enemy.y + enemy.speed
        elif ey > player.y:
            enemy.y = enemy.y - enemy.speed

    def move_enemy(self, player, enemy):
        if enemy.knock_back_timer == 0:
            if self.ai_type == 0:
                self.move_enemy_default(player, enemy)
            if self.ai_type == 1:
                self.move_enemy_aggressive(player, enemy)
        else:
            enemy.x -= enemy.knock_back_velocity_x
            enemy.y -= enemy.knock_back_velocity_y
            enemy.knock_back_timer -= 1

    def move_companion(self, player, companion):
        # companion stays near the player
        self.move_enemy_default(player, enemy=companion)
