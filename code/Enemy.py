from .Const import ENTITY_SPEED, WIN_HEIGHT
from .Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
        # Remove o inimigo quando sair da tela
        if self.rect.top > WIN_HEIGHT:
            self.health = 0