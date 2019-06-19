# 3rd party modules
import tcod as libtcod
import pygame
import random

# game file

import constants
import gui_elements
from entity import Entity


def random_turn(entity):
    roll_init = random.randint(0, entity.dice_pool)
    entity.set_init(entity.roll_dice(roll_init))
    roll_attack = random.randint(0, entity.dice_pool)
    entity.set_attack(entity.roll_dice(roll_attack))
    roll_defence = random.randint(0, entity.dice_pool)
    entity.set_defence(entity.roll_dice(roll_defence))


def draw_headers(surface):

    # HP
    text_hp_player_header = GAME_FONT.render('HP', True, constants.COLOR_GREEN)
    text_hp_npc_header = GAME_FONT.render('HP', True, constants.COLOR_GREEN)
    surface.blit(text_hp_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 200))
    surface.blit(text_hp_npc_header, (constants.NPC_X, constants.NPC_Y + 200))

    # INIT
    text_init_player_header = GAME_FONT.render('INIT', True, constants.COLOR_GREEN)
    text_init_npc_header = GAME_FONT.render('INIT', True, constants.COLOR_GREEN)
    surface.blit(text_init_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 250))
    surface.blit(text_init_npc_header, (constants.NPC_X, constants.NPC_Y + 250))

    # ATTACK
    text_atk_player_header = GAME_FONT.render('ATK', True, constants.COLOR_GREEN)
    text_atk_npc_header = GAME_FONT.render('ATK', True, constants.COLOR_GREEN)
    surface.blit(text_atk_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 300))
    surface.blit(text_atk_npc_header, (constants.NPC_X, constants.NPC_Y + 300))

    # DEFENCE
    text_def_player_header = GAME_FONT.render('DEF', True, constants.COLOR_GREEN)
    text_def_npc_header = GAME_FONT.render('DEF', True, constants.COLOR_GREEN)
    surface.blit(text_def_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 350))
    surface.blit(text_def_npc_header, (constants.NPC_X, constants.NPC_Y + 350))


def draw_game(surface, entity_player, entity_npc):

    # clear surface
    surface.fill(constants.COLOR_DEFAULT_BG)

    # draw character
    surface.blit(constants.STICK_PLAYER, (constants.PLAYER_X, constants.PLAYER_Y) )
    surface.blit(constants.STICK_NPC, (constants.NPC_X, constants.NPC_Y))

    # draw headers
    draw_headers(surface)


def game_main_loop():
    ''' In this function, we loop the main game '''
    global GAME_FONT

    # init pygame
    pygame.init()

    surface_main = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))

    # set font and size
    GAME_FONT = pygame.font.SysFont('New Times Roman', 32)


    # FIXME -  Generating random turns to test display
    player = Entity(6)
    npc = Entity(6)
    random_turn(player)
    random_turn(npc)

    game_quit = False

    # creates text boxes for hp, initiative, attack, defence
    button_player_hp = gui_elements.Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 200,
                                           50, 20)
    button_npc_hp = gui_elements.Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 200, 50, 20)

    button_player_init = gui_elements.Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 250,
                                           50, 20)
    button_npc_init = gui_elements.Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 250, 50, 20)
    button_player_attack = gui_elements.Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 300,
                                           50, 20)
    button_npc_attack = gui_elements.Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 300, 50, 20)
    button_player_defence = gui_elements.Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 350,
                                           50, 20)
    button_npc_defence = gui_elements.Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 350, 50, 20)


    while not game_quit:

        # wait for  player input
        event = pygame.event.wait()

        # process input
        if event.type == pygame.QUIT:
            game_quit = True






        # draw game

        draw_game(surface_main, player, npc)
        button_player_hp.draw(surface_main)
        button_npc_hp.draw(surface_main)
        button_player_init.draw(surface_main)
        button_npc_init.draw(surface_main)
        button_player_attack.draw(surface_main)
        button_npc_attack.draw(surface_main)
        button_player_defence.draw(surface_main)
        button_npc_defence.draw(surface_main)

        # update display and draw elements
        pygame.display.flip()

    # quit game
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_main_loop()

