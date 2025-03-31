from .Const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT
from .Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.initial_y = position[1]

    def move(self):
        # Move o background para BAIXO (+ em Y)
        self.rect.centery += ENTITY_SPEED[self.name]

        # Reinicia quando sair totalmente da tela (base)
        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = 0