import pygame
from pygame import Surface
from pygame.font import Font

from .Const import C_GREEN, C_WHITE, WIN_WIDTH, WIN_HEIGHT


class WinScreen:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def run(self):
        musica = pygame.mixer.Sound('./assets/Win.mp3')
        musica.play(loops=-1)

        try:
            win_sound = pygame.mixer.Sound('./assets/Win.wav')
            win_sound.play()
        except:
            pass

        while True:
            self.screen.blit(self.surf, self.rect)

            # Texto de vitória
            self.draw_text(50, "Congratulations!", C_GREEN, (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50))
            self.draw_text(30, "You Win!", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 20))
            self.draw_text(25, "Press ESPACE...", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 100))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True

    def draw_text(self, size: int, text: str, color: tuple, center_pos: tuple):
        font = Font(None, size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=center_pos)
        self.screen.blit(text_surf, text_rect)