import pygame

from src.tilesheet import TileSheet


class Assets:

    def __init__(self):
        self.player_images = [pygame.image.load(f"../assets/player/player_walk_{i}.png") for i in range(4)]
        self.slime_images = [pygame.image.load(f"../assets/enemies/slime/slime_animation_{i}.png") for i in range(4)]
        self.ass_images = [pygame.image.load(f"../assets/enemies/ass/schritt{i}_ass1.png") for i in range(1, 4)]
        self.snake_images = [pygame.image.load(f"../assets/enemies/snake/l0_schlangenmann{i}.png") for i in range(1, 3)]
        self.rock_tobi_images = [pygame.image.load(f"../assets/enemies/rock/rocktobi_{i}.png") for i in range(0, 2)]

        # sounds
        self.background_music = pygame.mixer.Sound("../assets/sounds/ohyeah.wav")
        self.peng_sound = pygame.mixer.Sound("../assets/sounds/peng.wav")
        self.hit_sound = pygame.mixer.Sound("../assets/sounds/aua.wav")
        self.tree = pygame.image.load("../assets/environment/tree.png")
        self.hit_0 = pygame.mixer.Sound("../assets/sounds/hit_0.wav")
        self.hit_1 = pygame.mixer.Sound("../assets/sounds/hit_1.wav")
        self.hit_2 = pygame.mixer.Sound("../assets/sounds/hit_2.wav")
        self.hit_3 = pygame.mixer.Sound("../assets/sounds/hit_3.wav")

        # buttons
        self.button_resume_img = pygame.image.load("../assets/buttons/button_resume.png")
        self.button_options_img = pygame.image.load("../assets/buttons/button_options.png")
        self.button_quit_img = pygame.image.load("../assets/buttons/button_quit.png")
        self.button_video_img = pygame.image.load("../assets/buttons/button_video.png")
        self.button_audio_img = pygame.image.load("../assets/buttons/button_audio.png")
        self.button_keys_img = pygame.image.load("../assets/buttons/button_keys.png")
        self.button_back_img = pygame.image.load("../assets/buttons/button_back.png")

        # tiles
        self.grass_tile_img = pygame.image.load("../assets/environment/grass.png")
        self.projectile_tile_img = pygame.image.load("../assets/projectiles/fire_bullet_16x16.png")

        self.grass_tile = TileSheet(image=self.grass_tile_img, tile_size=16, n_columns=25, n_rows=14, scale=(32, 32))
        self.projectile_tile = TileSheet(image=self.projectile_tile_img, tile_size=16, n_rows=25, n_columns=40)

        self.projectile_images = [self.projectile_tile.tile_table[i][1] for i in range(5)]

    def preprocess_images(self):
        self.tree = pygame.transform.scale(self.tree, (150, 250))
        self.player_images = [pygame.transform.scale(img, (42, 52)) for img in self.player_images]
        self.slime_images = [pygame.transform.scale(img, (32, 32)) for img in self.slime_images]
        self.snake_images = [pygame.transform.scale(img, (64, 64)) for img in self.snake_images]
        self.rock_tobi_images = [pygame.transform.scale(img, (64, 64)) for img in self.rock_tobi_images]

        # convert alpha
        self.button_resume_img = self.button_resume_img.convert_alpha()
        self.button_options_img = self.button_options_img.convert_alpha()
        self.button_quit_img = self.button_quit_img.convert_alpha()
        self.button_video_img = self.button_video_img.convert_alpha()
        self.button_audio_img = self.button_audio_img.convert_alpha()
        self.button_keys_img = self.button_keys_img.convert_alpha()
        self.button_back_img = self.button_back_img.convert_alpha()

    def preprocess_sounds(self):
        self.background_music.set_volume(0.3)
        self.hit_sound.set_volume(0.3)
        self.peng_sound.set_volume(0.2)
