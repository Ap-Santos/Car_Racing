import pygame
import random
import sys
from pygame import Surface
from pygame.font import Font

from .EntityFactory import EntityFactory
from .EntityMediator import EntityMediator
from .Player import Player
from .Const import C_WHITE, EVENT_ENEMY, EVENT_TIMEOUT, SPAWN_TIME, TIMEOUT_STEP, TIMEOUT_LEVEL, WIN_HEIGHT


class Level:
    def __init__(self, screen: Surface, name: str, game_mode: str):
        self.screen = screen
        self.name = name
        self.game_mode = game_mode
        self.entity_list = EntityFactory.get_entity(self.name + 'Bg') + [EntityFactory.get_entity('Player')]
        self.timeout = TIMEOUT_LEVEL
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self):
        level_music = pygame.mixer.Sound('./assets/Level1.mp3')
        level_music.play(loops=-1)

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    enemy = EntityFactory.get_entity(random.choice(('Enemy1', 'Enemy2')))
                    if enemy:
                        self.entity_list.append(enemy)
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        level_music.stop()
                        return  'win'
                    if not any(isinstance(ent, Player) for ent in self.entity_list):
                        return 'lose'

            for ent in self.entity_list:
                self.screen.blit(ent.surf, ent.rect)
                ent.move()

            EntityMediator.verify_colision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            if not any(isinstance(ent, Player) for ent in self.entity_list):
                level_music.stop()
                return False
            self.level_text(40, f'{self.name} - TIMEOUT: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        font = Font(None, text_size)
        text_surf = font.render(text, True, text_color)
        self.screen.blit(text_surf, text_pos)