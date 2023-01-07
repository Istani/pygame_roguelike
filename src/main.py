import random
import sys

import pygame

from src.player import Player
from src.projectile import Projectile
from src.creatures.slime import Slime
from src.gui import GUI

if __name__ == '__main__':

    pygame.font.init()
    pygame.mixer.init()
    music = pygame.mixer.Sound("../assets/sounds/ohyeah.wav")
    peng = pygame.mixer.Sound("../assets/sounds/peng.wav")
    aua = pygame.mixer.Sound("../assets/sounds/aua.wav")


    pygame.init()
    wight = 1920
    height = 1200
    n_enemies = 3
    max_enemies = 25
    stop = False

    display = pygame.display.set_mode((wight, height))
    clock = pygame.time.Clock()
    player = Player(wight // 2, height // 2, 42, 52, "Sandro")
    gui = GUI(display, player, center=[wight // 2, height // 2])

    tree = pygame.image.load("../assets/environment/tree.png")
    tree = pygame.transform.scale(tree, (150, 250))

    enemies = []
    player_projectiles = []
    enemy_projectiles = []

    display_scroll = [0, 0]

    music.play(loops=-1)
    music.set_volume(0.7)
    while True:

        keys = pygame.key.get_pressed()

        player_projectiles = [p for p in player_projectiles if p.alive]

        for e in enemies:
            if not e.alive:
                n_enemies += 2
        if n_enemies > max_enemies:
            n_enemies = max_enemies
        enemies = [e for e in enemies if e.alive]

        if len(enemies) < n_enemies:
            enemies += [Slime(random.randint(0, wight), random.randint(0, height), display)]

        display.fill((23, 164, 86))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    peng.play()
                    player_projectiles.append(
                        Projectile(x=player.x, y=player.y, y_mouse=mouse_y, x_mouse=mouse_x, size=25,
                                   speed=10))


        if keys[pygame.K_a]:
            display_scroll[0] -= 5
            for p in player_projectiles:
                p.x += 5
            player.animation_counter += 10
            player.moving_left = True
            player.moving_right = False
        if keys[pygame.K_d]:
            display_scroll[0] += 5
            for p in player_projectiles:
                p.x -= 5
            player.animation_counter += 10
            player.moving_right = True
            player.moving_left = False

        if keys[pygame.K_w]:
            display_scroll[1] -= 5
            for p in player_projectiles:
                p.x += 5
        if keys[pygame.K_s]:
            display_scroll[1] += 5
            for p in player_projectiles:
                p.x -= 5




        for p in player_projectiles:
            p.draw(display, enemies)
        for enemy in enemies:
            enemy.draw(display_scroll, player, player_projectiles, aua)

        player.draw(display)
        display.blit(tree, (100 - display_scroll[0], 100 - display_scroll[1], 16, 16))
        display.blit(tree, (300 - display_scroll[0], 300 - display_scroll[1], 16, 16))
        display.blit(tree, (100 - display_scroll[0], 600 - display_scroll[1], 16, 16))

        gui.draw()

        clock.tick(60)
        pygame.display.update()
