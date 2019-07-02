import pygame

pygame.init()

# Game sizes
GAME_WIDTH = 800
GAME_HEIGHT = 600

# Map Vars
PLAYER_X = 150
PLAYER_Y = 225
NPC_X = 525
NPC_Y = 225

# Color definitions
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GOLD = (255, 215, 0)
COLOR_MAGENTA = (255, 0, 255)
COLOR_CYAN = (0, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_LIGHT_YELLOW = (255, 255, 0)

# Game Colors
COLOR_DEFAULT_BG = COLOR_GREY

# Game Fonts
HEADER_FONT = pygame.font.SysFont('New Times Roman', 32)


# Sprites
STICK_PLAYER = pygame.image.load("data/player.png")
STICK_NPC = pygame.image.load("data/npc.png")

# Turn states
ATTACK_FIRST = ['attack', 'damage', 'defence']
DEFEND_FIRST = ['defence', 'attack', 'damage']
