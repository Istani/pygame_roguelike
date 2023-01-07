import pygame


class GUI:

    def __init__(self, display, player, center):
        self.main_font = pygame.font.SysFont("comicsans", 20)
        self.game_over_font = pygame.font.SysFont("comicsans", 100)
        self.credits = pygame.font.SysFont("comicsans", 30)

        self.display = display
        self.player = player
        self.center = center
        self.credit_str = "BobSan - programming * Dupomat - art * yunkeed - sound"

    def draw(self):
        if not self.player.alive:
            game_over = self.game_over_font.render("GAME OVER!", True, (255, 255, 255))
            self.display.blit(game_over, (self.center[0] - 400, self.center[1] - 250))
            self.display.blit(self.main_font.render(str(self.player.kills) + " kills", True, (255, 255, 255)),
                              (self.center[0], self.center[1]))
            return
        player_name = self.main_font.render(self.player.name, True, (255, 255, 255))
        kills = self.main_font.render(str(self.player.kills), True, (255, 255, 255))
        if self.player.live < 100:
            c = (255, 0, 0)
        else:
            c = (255, 255, 255)

        cd = self.credits.render(self.credit_str,True, (255, 255, 255))
        self.display.blit(cd,(self.center[0] - 400, 10))
        live = self.main_font.render(str(self.player.live) + " /100 HP", True, c)
        self.display.blit(player_name, (self.player.x - 15, self.player.y - 28))
        self.display.blit(live, (self.player.x - 15, self.player.y - 48))
        self.display.blit(kills, (50, 50))
