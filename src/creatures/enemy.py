import pygame


class Enemy:

    def __init__(self, x, y, display, animation_img_path_list, hit_sound_path):
        self.x = x
        self.y = y
        self.animation_images = [pygame.image.load(img) for img in animation_img_path_list]
        self.mask = pygame.mask.from_surface(self.animation_images[0])
        self.animation_count = 0
        self.reset_offset = 0
        self.display = display
        self.alive = True
        self.hit_sound = pygame.mixer.Sound(hit_sound_path)

    def draw(self, display_scroll, player, player_projectiles, aua):
        if not self.alive:
            return
        for p in player_projectiles:
            offset_x = p.x - self.x + display_scroll[0]
            offset_y = p.y - self.y + display_scroll[1]
            if p.mask.overlap(self.mask, (offset_x, offset_y)) is not None:
                player.width += 1
                player.height += 1
                self.alive = False
                p.alive = False
                player.kills += 1
                aua.play()

        # player dmg?
        offset_x = player.x - self.x + display_scroll[0]
        offset_y = player.y - self.y + display_scroll[1]
        if player.mask.overlap(self.mask, (offset_x, offset_y)) is not None:
            player.live -= 1


        if self.animation_count + 1 == 16:
            self.animation_count = 0
        self.animation_count += 1

        self.display.blit(pygame.transform.scale(self.animation_images[self.animation_count // 4], (64, 64)),
                          (self.x - display_scroll[0], self.y - display_scroll[1]))
