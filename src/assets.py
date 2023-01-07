import pygame


class Assets:

    def __init__(self):
        self.player_images = [pygame.image.load(f"../assets/player/player_walk_{i}.png") for i in range(4)]
        self.slime_images = [pygame.image.load(f"../assets/slime/slime_animation_{i}.png") for i in range(4)]
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

