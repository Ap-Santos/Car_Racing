import pygame
from .Menu import Menu
from .Level import Level
from .Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from .WinScreen import WinScreen


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Car Racing")
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.screen)
            option = menu.run()

            if option == MENU_OPTION[0]:  # NEW GAME
                level = Level(self.screen, 'Level1', option)
                result = level.run()

                if result == 'win':
                    win_screen = WinScreen(self.screen)
                    win_screen.run()

            elif option == MENU_OPTION[1]:  # EXIT
                pygame.quit()
                return