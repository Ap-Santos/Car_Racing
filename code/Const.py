# Cores
import pygame

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (238, 173, 45)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# Entidades
ENTITY_DAMAGE = {
    'Level1Bg': 0,
    'Player': 0,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
}

ENTITY_HEALTH = {
    'Level1Bg': 999,
    'Player': 3,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
}

ENTITY_SPEED = {
    'Level1Bg': 5,
    'Player': 8,
    'Enemy1': 4,
    'Enemy2': 4,
    'Enemy3': 4
}

# Eventos
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# Menu
MENU_OPTION = ('NEW GAME', 'EXIT')

# Controles
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}

# Configurações
SPAWN_TIME = 3000
TIMEOUT_STEP = 1
TIMEOUT_LEVEL = 60000
WIN_WIDTH = 840
WIN_HEIGHT = 650
