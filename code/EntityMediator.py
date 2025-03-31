from .Const import WIN_WIDTH
from .Enemy import Enemy
from .Player import Player

class EntityMediator:
    @staticmethod
    def __verify_colision_window(ent):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, Player):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_colision_entity(ent1, ent2):
        valid_interaction = isinstance(ent1, Enemy) and isinstance(ent2, Player) or \
                           isinstance(ent1, Player) and isinstance(ent2, Enemy)

        if valid_interaction and ent1.rect.colliderect(ent2.rect):
            ent1.health -= ent2.damage
            ent2.health -= ent1.damage
            ent1.last_dmg = ent2.name
            ent2.last_dmg = ent1.name

    @staticmethod
    def verify_colision(entity_list):
        for i, entity1 in enumerate(entity_list):
            EntityMediator.__verify_colision_window(entity1)
            for entity2 in entity_list[i+1:]:
                EntityMediator.__verify_colision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list):
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]