import pygame


class Assets:

    def __init__(self):
        self.player_images = [pygame.image.load(f"../assets/player/player_walk_{i}.png") for i in range(4)]
        self.slime_images = [pygame.image.load(f"../assets/enemies/slime/slime_animation_{i}.png") for i in range(4)]
        self.penis_images = [pygame.image.load(f"../assets/enemies/penis/l0_sprite_{i}.png") for i in range(1, 6)]
        self.ass_images = [pygame.image.load(f"../assets/enemies/ass/schritt{i}_ass1.png") for i in range(1, 4)]
        self.snake_images = [pygame.image.load(f"../assets/enemies/snake/l0_schlangenmann{i}.png") for i in range(1, 3)]
        self.background_music = pygame.mixer.Sound("../assets/sounds/ohyeah.wav")
        self.peng_sound = pygame.mixer.Sound("../assets/sounds/peng.wav")
        self.hit_sound = pygame.mixer.Sound("../assets/sounds/aua.wav")
        self.tree = pygame.image.load("../assets/environment/tree.png")
        self.projectile_images = [pygame.image.load(f"../assets/projectiles/fire_bullet_{i}.png") for i in range(1, 4)]

        self.preprocess_images()

    def preprocess_images(self):
        self.tree = pygame.transform.scale(self.tree, (150, 250))
        self.player_images = [pygame.transform.scale(img, (42, 52)) for img in self.player_images]
        self.slime_images = [pygame.transform.scale(img, (32, 32)) for img in self.slime_images]
        self.projectile_images = [pygame.transform.scale(img, (20, 20)) for img in self.projectile_images]
        self.penis_images = [pygame.transform.scale(img, (64, 64)) for img in self.penis_images]
        self.snake_images = [pygame.transform.scale(img, (64, 64)) for img in self.snake_images]


