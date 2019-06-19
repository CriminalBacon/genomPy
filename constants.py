import pygame

pygame.init()

# Game sizes
GAME_WIDTH = 800
GAME_HEIGHT = 600

# Map Vars
PLAYER_X = 200
PLAYER_Y = 100
NPC_X = 500
NPC_Y = 100

# Color definitions
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GOLD = (255, 215, 0)

# Game Colors
COLOR_DEFAULT_BG = COLOR_GREY


# Sprites
STICK_PLAYER = pygame.image.load("data/player.png")
STICK_NPC = pygame.image.load("data/npc.png")
