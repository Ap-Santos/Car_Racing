import random
from .Background import Background
from .Enemy import Enemy
from .Player import Player
from .Const import  WIN_HEIGHT

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        if entity_name == 'Level1Bg':
            return [
                Background('Level1Bg', (0, 0)),
                Background('Level1Bg', (0,-WIN_HEIGHT))
            ]
        elif entity_name == 'Player':
            return Player('Player', (220, WIN_HEIGHT / 2))
        elif entity_name == 'Enemy1':
            return Enemy('Enemy1', (204, 0 +10))
        elif entity_name == 'Enemy2':
            return Enemy('Enemy2', (523, 0+10,))
        elif entity_name == 'Enemy3':
            return Enemy('Enemy3', (330, 0 + 10,))
        return None