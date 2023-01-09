import random
from perlin_noise import PerlinNoise
import pygame


class World:

    def __init__(self):
        self.enemies = []
        self.players = []
        self.projectiles = []
        self.trees = []
        self.noise = PerlinNoise(octaves=6, seed=random.randint(0, 100000))

    def check_collisions(self, display_scroll_x, display_scroll_y, use_rect=True):
        for projectile in self.projectiles:
            for enemy in self.enemies:
                offset_x = projectile.x - enemy.x - display_scroll_x
                offset_y = projectile.y - enemy.y - display_scroll_y
                if projectile.mask.overlap(enemy.mask, (offset_x, offset_y)) is not None:
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
                    enemy.rect.x = enemy.x + display_scroll_x
                    enemy.rect.y = enemy.y + display_scroll_y
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

    def draw_background(self, display_scroll_x, display_scroll_y, screen):
        tile_scaling = 40
        pos_x = int(display_scroll_x / 5)
        pos_y = int(display_scroll_y / 5)
        pix_x = int(pygame.display.get_window_size()[0] / tile_scaling)
        pix_y = int(pygame.display.get_window_size()[1] / tile_scaling)
        min_x, max_x = pos_x - pix_x, pos_x + pix_x
        min_y, max_y = pos_y - pix_y, pos_y + pix_y
        # self.pic = [[self.noise([i/self.xpix, j/self.ypix]) for j in range(self.xpix)] for i in range(self.ypix)]
        self.pic = [[self.noise([i / pix_x, j / pix_y]) for j in range(min_x, max_x)] for i in range(min_y, max_y)]
        for i, row in enumerate(self.pic):
            for j, column in enumerate(row):
                if column >= 0.6:
                    pygame.draw.rect(screen, (250, 250, 250),
                                     pygame.Rect(j * tile_scaling, i * tile_scaling, tile_scaling, tile_scaling))
                elif column >= 0.2:
                    pygame.draw.rect(screen, (80, 80, 80),
                                     pygame.Rect(j * tile_scaling, i * tile_scaling, tile_scaling, tile_scaling))
                elif column >= 0.09:
                    pygame.draw.rect(screen, (30, 90, 30),
                                     pygame.Rect(j * tile_scaling, i * tile_scaling, tile_scaling, tile_scaling))
                elif column >= 0.009:
                    pygame.draw.rect(screen, (10, 100, 10),
                                     pygame.Rect(j * tile_scaling, i * tile_scaling, tile_scaling, tile_scaling))
                elif column >= 0.002:
                    pygame.draw.rect(screen, (100, 150, 0),
                                     pygame.Rect(j * tile_scaling, i * tile_scaling, tile_scaling, tile_scaling))
                elif column >= -0.06:
                    pygame.draw.rect(screen, (30, 190, 0),
                                     pygame.Rect(j * tile_scaling, i * tile_scaling, tile_scaling, tile_scaling))
                elif column >= -0.02:
                    pygame.draw.rect(screen, (40, 200, 0),
                                     pygame.Rect(j * tile_scaling, i * tile_scaling, tile_scaling, tile_scaling))
                elif column >= -0.1:
                    pygame.draw.rect(screen, (10, 210, 0),
                                     pygame.Rect(j * tile_scaling, i * tile_scaling, tile_scaling, tile_scaling))
                elif column >= -0.8:
                    pygame.draw.rect(screen, (0, 0, 200),
                                     pygame.Rect(j * tile_scaling, i * tile_scaling, tile_scaling, tile_scaling))

    def draw(self, display_scroll_x, display_scroll_y, screen, use_perlin_noise=False):
        self.remove_dead_objects()
        self.move_enemies()
        if use_perlin_noise:
            self.draw_background(display_scroll_x, display_scroll_y, screen)
        for tree in self.trees:
            tree.draw(display_scroll_x, display_scroll_y)
        for projectile in self.projectiles:
            projectile.draw()
        for enemy in self.enemies:
            enemy.draw(display_scroll_x, display_scroll_y)
        for player in self.players:
            player.draw()
