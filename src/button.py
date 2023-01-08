import pygame
import sys


class Button:

    def __init__(self, image, x, y, display):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.x = x
        self.y = y
        self.display = display

    def action(self):
        pass

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.action()
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.display.blit(self.image, (self.x, self.y))
        return action


class ButtonResume(Button):

    def __init__(self, image, x, y, state, display):
        self.state = state
        super().__init__(image, x, y, display)

    def action(self):
        self.state.show_menu = False
        self.state.pause = False
        if self.state.game_over:
            self.state.reset_game = True
        self.state.play = True


class ButtonQuite(Button):

    def __init__(self, image, x, y, state, display):
        self.state = state
        super().__init__(image, x, y, display)

    def action(self):
        pygame.quit()
        sys.exit()
