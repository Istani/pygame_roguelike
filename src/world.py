
class World:

    def __init__(self):
        self.enemies = []
        self.players = []
        self.projectiles = []
        self.trees = []

    def check_collisions(self, display_scroll):
        for projectile in self.projectiles:
            for enemy in self.enemies:
                offset_x = projectile.x - enemy.x + display_scroll[0]
                offset_y = projectile.y - enemy.y + display_scroll[1]
                if projectile.mask.overlap(enemy.mask, (offset_x, offset_y)) is not None:
                    enemy.hit_sound.play()
                    enemy.alive = False
                    projectile.alive = False
                    projectile.player.kills += 1

        for player in self.players:
            for enemy in self.enemies:
                offset_x = player.x - enemy.x + display_scroll[0]
                offset_y = player.y - enemy.y + display_scroll[1]
                if player.mask.overlap(enemy.mask, (offset_x, offset_y)) is not None:
                    player.live -= 1

    def draw(self, display_scroll_x, display_scroll_y):
        for tree in self.trees:
            tree.draw(display_scroll_x, display_scroll_y)
        for projectile in self.projectiles:
            projectile.draw()
        for enemy in self.enemies:
            enemy.draw(display_scroll_x, display_scroll_y)
        for player in self.players:
            player.draw()

