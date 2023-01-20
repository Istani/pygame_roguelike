import pygame

from button import ButtonResume, ButtonQuite


class Menu:

    def __init__(self, display, center_x, center_y, assets, state):
        self.font = pygame.font.SysFont("comicsans", 20)
        self.play_button = self.font.render("PLAY", True, (255, 255, 255))
        self.settings_button = self.font.render("SETTINGS", True, (255, 255, 255))
        self.leaderboard_button = self.font.render("BOARD", True, (255, 255, 255))
        self.credits_button = self.font.render("CREDITS", True, (255, 255, 255))
        self.display = display
        self.center_x = center_x
        self.center_y = center_y
        self.center_text = pygame.font.SysFont("comicsans", 75)
        self.assets = assets
        self.state = state

        self.button_resume = ButtonResume(image=assets.button_resume_img, x=center_x - 50, y=center_y, state=self.state, display=self.display)
        self.button_quit = ButtonQuite(image=assets.button_quit_img, x=center_x - 50, y=center_y + 100, state=self.state, display=self.display)
        """
        self.button_options = Button(image=assets.button_options_img)

        self.button_video = Button(image=assets.button_video_img)
        self.button_audio = Button(image=assets.button_audio_img)
        self.button_keys = Button(image=assets.button_keys_img)
        self.button_back = Button(image=assets.button_back_img)
        """

    def draw_space_to_start(self):
        img = self.center_text.render("Press SPACE to start...", True, (255, 255, 255))
        self.display.blit(img, (self.center_x - 350, self.center_y))

    def draw_main_menu(self):
        pygame.draw.rect(self.display, (255, 255, 0), [self.center_x - 40, self.center_y - 40, 600, 500], 20)

        self.button_resume.draw()
        self.button_quit.draw()
