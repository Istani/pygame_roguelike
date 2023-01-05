import pygame


class GUI:

    def __init__(self, display, player):
        self.main_font = pygame.font.SysFont("comicsans", 20)
        self.display = display
        self.player = player

    def draw(self):
        player_name = self.main_font.render(self.player.name, True, (255, 255, 255))
        self.display.blit(player_name, (self.player.x - 15, self.player.y -28))
