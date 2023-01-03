import sys
from src.player import Player

import pygame as pg

if __name__ == '__main__':
    pg.init()

    display = pg.display.set_mode((1600, 800))
    clock = pg.time.Clock()
    player = Player(800, 400, 32, 32)

    while True:
        display.fill((0, 0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        player.draw(display)

        clock.tick(60)
        pg.display.update()
