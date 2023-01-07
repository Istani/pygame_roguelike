class World:

    def __init__(self):
        self.player = None
        self.enemies = []
        self.player_p

    @staticmethod
    def is_collision(projectile, enemy, display_scroll):
        offset_x = projectile.x - enemy.x + display_scroll[0]
        offset_y = projectile.y - enemy.y + display_scroll[1]
        if projectile.mask.overlap(enemy.mask, (offset_x, offset_y)) is not None:
            return True
        return False

    def check_collisions(self, enemies, projectiles, display_scroll):
        for projectile in projectiles:
            for enemy in enemies:
                if self.is_collision(enemy=enemy, projectile=projectile, display_scroll=display_scroll):
                    enemy.alive = False
                    projectile.alive = False
                    projectile.player.kills += 1
