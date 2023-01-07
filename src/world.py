class World:

    def __init__(self):
        self.enemies = []
        self.players = []
        self.projectiles = []
        self.trees = []

    def check_collisions(self, display_scroll_x, display_scroll_y):
        for projectile in self.projectiles:
            for enemy in self.enemies:
                offset_x = projectile.x - enemy.x + display_scroll_x
                offset_y = projectile.y - enemy.y + display_scroll_y
                if projectile.mask.overlap(enemy.mask, (offset_x, offset_y)) is not None:
                    if enemy.alive:
                        enemy.hit_sound.play()
                    enemy.alive = False
                    projectile.alive = False
                    projectile.player.kills += 1

        for player in self.players:
            for enemy in self.enemies:
                offset_x = player.x - enemy.x + display_scroll_x
                offset_y = player.y - enemy.y + display_scroll_y
                if player.mask.overlap(enemy.mask, (offset_x, offset_y)) is not None:
                    player.live -= 1

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.ai.move_enemy(player=self.players[0], enemy=enemy)

    def remove_dead_objects(self):
        self.enemies = [e for e in self.enemies if e.alive]
        self.projectiles = [p for p in self.projectiles if p.alive]

    def draw(self, display_scroll_x, display_scroll_y):
        self.remove_dead_objects()
        self.move_enemies()
        for tree in self.trees:
            tree.draw(display_scroll_x, display_scroll_y)
        for projectile in self.projectiles:
            projectile.draw()
        for enemy in self.enemies:
            enemy.draw(display_scroll_x, display_scroll_y)
        for player in self.players:
            player.draw()


