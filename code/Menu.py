import sys

import pygame
from pygame import Surface
from pygame.font import Font

from .Const import C_ORANGE, C_WHITE, C_YELLOW, MENU_OPTION, WIN_WIDTH, WIN_HEIGHT


class Menu:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(left=0, top=0)
        self.screen = screen
        self.surf = pygame.transform.scale(
            pygame.image.load('./assets/MenuBg.png').convert_alpha(),
            (WIN_WIDTH, WIN_HEIGHT)
        )
        self.rect = self.surf.get_rect(left=0, top=0)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font = Font(None, text_size)
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(text_surf, text_rect)

    def run(self):
        menu_option = 0
        musica = pygame.mixer.Sound('./assets/Menu.mp3')
        musica.play(loops=-1)

        while True:
            self.screen.blit(self.surf, self.rect)
            self.menu_text(90, "Car", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(90, "Racing", C_ORANGE, ((WIN_WIDTH / 2), 120))

            for i, option in enumerate(MENU_OPTION):
                color = C_YELLOW if i == menu_option else C_WHITE
                self.menu_text(30, option, color, (WIN_WIDTH / 2, 200 + 50 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        musica.stop()
                        return MENU_OPTION[menu_option]
