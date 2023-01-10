import pygame


class World:

    def __init__(self, draw_trees=False):
        self.enemies = []
        self.players = []
        self.projectiles = []
        self.trees = []
        self.draw_trees = draw_trees

    def check_collisions(self, display_scroll_x, display_scroll_y, use_rect=True):
        for projectile in self.projectiles:
            for enemy in self.enemies:
                collision = False
                if use_rect:
                    enemy.rect.x = enemy.x - display_scroll_x
                    enemy.rect.y = enemy.y - display_scroll_y
                    if projectile.rect.colliderect(enemy.rect):
                        collision = True
                else:
                    offset_x = projectile.x - enemy.x - display_scroll_x
                    offset_y = projectile.y - enemy.y - display_scroll_y
                    if projectile.mask.overlap(enemy.mask, (offset_x, offset_y)) is not None:
                        collision = True
                if collision:
                    if enemy.alive:
                        enemy.hit_sound.play()
                    enemy.alive = False
                    projectile.alive = False
                    projectile.player.kills += 1

        for player in self.players:
            player.rect.x = player.x
            player.rect.y = player.y
            for enemy in self.enemies:
                collision = False
                if use_rect:
                    enemy.rect.x = enemy.x - display_scroll_x
                    enemy.rect.y = enemy.y - display_scroll_y
                    if player.rect.colliderect(enemy.rect):
                        collision = True
                else:
                    offset_x = player.x - enemy.x + display_scroll_x
                    offset_y = player.y - enemy.y + display_scroll_y
                    if player.mask.overlap(enemy.mask, (offset_x, offset_y)) is not None:
                        collision = True
                if collision:
                    player.live -= 1

    def enemy_would_collide(self, enemy):
        for e in self.enemies:
            if e != enemy:
                offset_x = e.x - enemy.x
                offset_y = e.y - enemy.y
                if e.mask.overlap(enemy.mask, (offset_x, offset_y)) is not None:
                    return True
        return False

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.ai.move_enemy(player=self.players[0], enemy=enemy)

    def remove_dead_objects(self):
        self.enemies = [e for e in self.enemies if e.alive]
        self.projectiles = [p for p in self.projectiles if p.alive]

    def draw(self, display_scroll_x, display_scroll_y, screen):
        self.remove_dead_objects()
        self.move_enemies()
        if self.draw_trees:
            for tree in self.trees:
                tree.draw(display_scroll_x, display_scroll_y)
        for projectile in self.projectiles:
            projectile.draw()
        for enemy in self.enemies:
            enemy.draw(display_scroll_x, display_scroll_y)
        for player in self.players:
            player.draw()
