import pygame
from .Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT,PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT # PLAYER_KEY_UP, PLAYER_KEY_DOWN,
from .Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def carSound(self):
       pass


    def move(self):
        self.carSound()
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 130:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        elif pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH -130:
            self.rect.centerx += ENTITY_SPEED[self.name]