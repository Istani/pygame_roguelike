import pygame
import sys
import random
import os

from src.world import World
from src.assets import Assets
from src.player import Player
from src.gui import GUI
from src.projectile import Projectile
from src.natureobject import Tree
from src.enemy import Enemy
from src.ai import AI
from src.menu import Menu
from src.state import State
from src.map import Map

class Game:

    def __init__(self, wight=1920, height=1200, fps=60, dev_view=False, use_player_gui=False):
        self.dev_view = dev_view
        self.player_name = os.environ.get('USERNAME')
        pygame.font.init()
        pygame.mixer.init()
        self.assets = Assets()
        pygame.init()
        self.display = pygame.display.set_mode((wight, height))
        self.assets.preprocess_images()
        self.assets.preprocess_sounds()
        self.word = None
        self.wight = wight
        self.height = height
        self.n_enemies = 100
        self.n_trees = 3
        self.clock = pygame.time.Clock()
        self.center_x = self.wight // 2
        self.center_y = self.height // 2
        self.player = None
        self.gui = None
        self.state = None
        self.background_color = (23, 144, 86)
        self.fps = fps
        self.init_spawn()
        self.menu = Menu(display=self.display, center_x=self.center_x, center_y=self.center_y, assets=self.assets,
                         state=self.state)
        self.spawn_counter = 60
        self.spawn_counter_index = 0
        self.use_player_gui = use_player_gui
        self.map = Map(tile_table=self.assets.grass_tile.get_tile_table())

    def init_spawn(self):
        self.player = Player(self.center_x, self.center_y, self.player_name, self.assets.player_images, self.display)
        self.gui = GUI(self.display, self.player, center=[self.center_x, self.center_y])
        self.word = World(assets=self.assets, dev_view=self.dev_view)
        self.word.players.append(self.player)

        for _ in range(self.n_trees):
            self.word.trees.append(Tree(display=self.display, x=random.randint(0, self.wight),
                                        y=random.randint(0, self.height), image=self.assets.tree))
        self.state = State()

    def spawn_random_enemy(self):
        rd = random.randint(1, 5)
        if rd == 1:
            enemy_sprite = self.assets.penis_images
            speed = 1
            ai_nr = 1
            hit_sound = self.assets.hit_0
            fire = True
        elif rd == 2:
            enemy_sprite = self.assets.ass_images
            speed = 2
            ai_nr = 1
            hit_sound = self.assets.hit_1
            fire = True
        elif rd == 3:
            enemy_sprite = self.assets.snake_images
            speed = 2
            ai_nr = 0
            hit_sound = self.assets.hit_2
            fire = False
        elif rd == 4:
            enemy_sprite = self.assets.slime_images
            speed = 1
            ai_nr = 0
            hit_sound = self.assets.hit_3
            fire = False
        else:
            enemy_sprite = self.assets.rock_tobi_images
            speed = 1
            ai_nr = 0
            hit_sound = self.assets.hit_3
            fire = False
        self.word.enemies.append(
            Enemy(display=self.display, enemy_images=enemy_sprite, hit_sound=hit_sound,
                  ai=AI(ai_type=ai_nr), speed=speed, display_scroll_x=self.player.display_scroll_x,
                  display_scroll_y=self.player.display_scroll_y, dev_view=self.dev_view, uses_projectiles=fire))

    def spawn_enemies(self):
        if self.spawn_counter_index == self.spawn_counter:
            self.spawn_counter_index = -1
            if len(self.word.enemies) < self.n_enemies:
                self.spawn_random_enemy()
        self.spawn_counter_index += 1

    def game_loop_step(self, events):
        self.spawn_enemies()
        keys = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    if self.player.alive:
                        self.assets.peng_sound.play()
                        self.word.projectiles.append(
                            Projectile(y_mouse=mouse_y, x_mouse=mouse_x, player=self.player, speed=10,
                                       animation_images=self.assets.projectile_images, dev_view=self.dev_view))
        self.word.check_collisions(self.player.display_scroll_x, self.player.display_scroll_y)
        self.player.move(keys)
        self.word.draw(self.player.display_scroll_x, self.player.display_scroll_y)
        if self.use_player_gui:
            self.gui.draw()

    def main_loop(self):
        self.assets.background_music.play(loops=-1)
        while True:
            self.display.fill(self.background_color)
            self.map.draw(self.display, self.player.display_scroll_x, self.player.display_scroll_y)

            if self.state.reset_game:
                self.init_spawn()
                self.state.reset_game = False
                self.state.play = True
                self.state.show_menu = False
                self.state.game_over = False
            if not self.player.alive:
                self.state.game_over = True
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.state.game_over:
                        self.state.show_menu = True
                    if event.key == pygame.K_SPACE:
                        self.state.pause = not self.state.pause
                    if event.key == pygame.K_ESCAPE:
                        self.state.pause = False
                        self.state.play = False
                        self.state.show_menu = True
            if self.state.show_menu:
                self.menu.draw_main_menu()
            elif self.state.pause:
                self.menu.draw_space_to_start()

            else:
                self.game_loop_step(events)
            self.clock.tick(self.fps)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.main_loop()
