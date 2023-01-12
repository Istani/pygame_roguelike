import pygame


class World:

    def __init__(self, assets, draw_trees=False, dev_view=False):
        self.enemies = []
        self.players = []
        self.projectiles = []
        self.trees = []
        self.draw_trees = draw_trees
        self.assets = assets
        self.enemies_projectiles = []
        self.dev_view = dev_view

    def enemies_fire_projectiles(self):
        for enemy in self.enemies:
            if enemy.uses_projectiles:
                new_projectile = enemy.fire_projectile(animation_images=self.assets.projectile_images,
                                                       player=self.players[0])
                if new_projectile is not None:
                    self.enemies_projectiles.append(new_projectile)

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
                    enemy.live -= projectile.damage
                    if enemy.live <= 0:
                        enemy.alive = False
                        projectile.player.kills += 1
                    projectile.alive = False
                    enemy.knock_back_velocity_x = projectile.x_vel
                    enemy.knock_back_velocity_y = projectile.y_vel
                    enemy.knock_back_timer = projectile.knock_back_duration

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
                    if not self.dev_view:
                        player.live -= 1

            for enemy_projectile in self.enemies_projectiles:
                if player.rect.colliderect(enemy_projectile.rect):
                    if enemy_projectile.alive and player.alive:
                        if not self.dev_view:
                            player.live -= enemy_projectile.damage
                        enemy_projectile.alive = False
                        self.assets.hit_sound.play()

    def enemy_would_collide_old(self, enemy):
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
        self.enemies_projectiles = [ep for ep in self.enemies_projectiles if ep.alive]
        self.enemies = [e for e in self.enemies if e.alive]
        self.projectiles = [p for p in self.projectiles if p.alive]

    def draw(self, display_scroll_x, display_scroll_y):
        self.remove_dead_objects()
        self.move_enemies()
        self.enemies_fire_projectiles()
        if self.draw_trees:
            for tree in self.trees:
                tree.draw(display_scroll_x, display_scroll_y)
        for projectile in self.projectiles:
            projectile.draw()
        for enemy in self.enemies:
            enemy.draw(display_scroll_x, display_scroll_y)
        for projectile in self.enemies_projectiles:
            projectile.draw(display_scroll_x, display_scroll_y)
        for player in self.players:
            player.draw()
