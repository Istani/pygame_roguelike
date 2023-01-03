import sys

import pygame

from src.player import Player
from src.projectile import Projectile

if __name__ == '__main__':
    pygame.init()

    display = pygame.display.set_mode((1600, 800))
    clock = pygame.time.Clock()
    player = Player(800, 400, 32, 32)
    player_projectiles = []

    display_scroll = [0, 0]

    while True:
        display.fill((0, 0, 0))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_projectiles.append(Projectile(x=player.x, y=player.y, y_mouse=mouse_y, x_mouse=mouse_x))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            display_scroll[0] -= 5
            for p in player_projectiles:
                p.x += 5
        if keys[pygame.K_d]:
            display_scroll[0] += 5
            for p in player_projectiles:
                p.x -= 5
        if keys[pygame.K_w]:
            display_scroll[1] -= 5
            for p in player_projectiles:
                p.x += 5
        if keys[pygame.K_s]:
            display_scroll[1] += 5
            for p in player_projectiles:
                p.x -= 5

        for p in player_projectiles:
            p.draw(display)
        pygame.draw.rect(display, (255, 255, 255), (100 - display_scroll[0], 100 - display_scroll[1], 16, 16))
        player.draw(display)

        clock.tick(60)
        pygame.display.update()
