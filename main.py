import sys

import pygame as pg

if __name__ == '__main__':
    pg.init()

    display = pg.display.set_mode((1600, 800))
    clock = pg.time.Clock()

    while True:
        display.fill((0,0,0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        clock.tick(60)
        pg.display.update()