import random

from src.projectile import CompanionProjectile


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
        self.items = []
        self.companions = []
        self.companion_projectiles = []

    def enemies_fire_projectiles(self):
        for enemy in self.enemies:
            if enemy.uses_projectiles:
                new_projectile = enemy.fire_projectile(player=self.players[0])
                if new_projectile is not None:
                    enemy.shot_sound.play()
                    self.enemies_projectiles.append(new_projectile)

    def companions_fire_projectiles(self):
        for companion in self.companions:
            if len(self.enemies) == 0:
                return
            if not companion.fire_projectile():
                continue
            target = random.choice(self.enemies)
            new_projectile = CompanionProjectile(companion=companion, enemy=target,
                                                 animation_images=self.assets.projectiles_player)
            companion.shot_sound.play()
            self.companion_projectiles.append(new_projectile)

    def check_collisions(self, display_scroll_x, display_scroll_y):
        for projectile in self.projectiles:
            for enemy in self.enemies:
                collision = False
                enemy.rect.x = enemy.x - display_scroll_x
                enemy.rect.y = enemy.y - display_scroll_y
                if projectile.rect.colliderect(enemy.rect):
                    collision = True
                if collision:
                    if enemy.alive:
                        enemy.hit_sound.play()
                    enemy.live -= projectile.damage
                    if enemy.live <= 0:
                        enemy.alive = False
                        projectile.player.kills += 1
                        loot = enemy.drop_loot()
                        if loot is not None:
                            self.items.append(loot)
                    projectile.alive = False
                    enemy.knock_back_velocity_x = projectile.x_vel
                    enemy.knock_back_velocity_y = projectile.y_vel
                    enemy.knock_back_timer = projectile.knock_back_duration

        for projectile in self.companion_projectiles:

            projectile.rect.x = projectile.x - display_scroll_x
            projectile.rect.y = projectile.y - display_scroll_y

            for enemy in self.enemies:

                enemy.rect.x = enemy.x - display_scroll_x
                enemy.rect.y = enemy.y - display_scroll_y

                if projectile.rect.colliderect(enemy.rect):
                    if not enemy.alive:
                        continue
                    enemy.hit_sound.play()
                    enemy.live -= projectile.damage
                    if enemy.live <= 0:
                        enemy.alive = False
                        projectile.player.kills += 1
                        loot = enemy.drop_loot()
                        if loot is not None:
                            self.items.append(loot)
                    projectile.alive = False
                    enemy.knock_back_velocity_x = projectile.x_vel
                    enemy.knock_back_velocity_y = projectile.y_vel
                    enemy.knock_back_timer = projectile.knock_back_duration

        for player in self.players:
            player.rect.x = player.x
            player.rect.y = player.y
            for enemy in self.enemies:
                collision = False
                enemy.rect.x = enemy.x - display_scroll_x
                enemy.rect.y = enemy.y - display_scroll_y
                if player.rect.colliderect(enemy.rect):
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

            for item in self.items:
                item.rect.x = item.x - display_scroll_x
                item.rect.y = item.y - display_scroll_y
                if player.rect.colliderect(item.rect):
                    if item.alive:
                        player.live += item.increase_live_points_by
                        if player.live > player.max_live:
                            player.live = player.max_live
                        item.alive = False

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.ai.move_enemy(player=self.players[0], enemy=enemy)

    def move_companions(self):
        for companion in self.companions:
            companion.ai.move_companion(self.players[0], companion)

    def remove_dead_objects(self):
        self.enemies_projectiles = [ep for ep in self.enemies_projectiles if ep.alive]
        self.enemies = [e for e in self.enemies if e.alive]
        self.projectiles = [p for p in self.projectiles if p.alive]
        self.items = [i for i in self.items if i.alive]
        self.companions = [c for c in self.companions if c.alive]

    def remove_out_of_screen_projectiles(self):
        pass

    def draw(self, display_scroll_x, display_scroll_y):
        self.remove_dead_objects()
        self.move_enemies()
        self.move_companions()
        self.enemies_fire_projectiles()
        self.companions_fire_projectiles()
        if self.draw_trees:
            for tree in self.trees:
                tree.draw(display_scroll_x, display_scroll_y)
        for projectile in self.projectiles:
            projectile.draw(display_scroll_x, display_scroll_y)
        for projectile in self.companion_projectiles:
            projectile.draw(display_scroll_x, display_scroll_y)
        for item in self.items:
            item.draw(display_scroll_x, display_scroll_y)
        for enemy in self.enemies:
            enemy.draw(display_scroll_x, display_scroll_y)
        for companion in self.companions:
            companion.draw(display_scroll_x, display_scroll_y)
        for projectile in self.enemies_projectiles:
            projectile.draw(display_scroll_x, display_scroll_y)
        for player in self.players:
            player.draw()
