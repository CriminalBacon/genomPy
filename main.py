# 3rd party modules
import tcod as libtcod
import pygame
import random

# game file

import constants
import gui_elements
from entity import Entity
import dice_tools


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

    # initialize dice count
    dice_count = 0

    # initialize game state
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

    button_roll_dice = gui_elements.Button(constants.COLOR_BLUE, constants.PLAYER_X + 175, constants.PLAYER_Y + 400,
                                           100, 50, "Roll")
    button_dice_number = gui_elements.Button(constants.COLOR_GOLD, constants.PLAYER_X + 100, constants.PLAYER_Y + 400,
                                             40, 40)

    while not game_quit:

        ##### wait for  player input
        # event = pygame.event.wait()

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            # process input
            if event.type == pygame.QUIT:
                game_quit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_roll_dice.is_over(mouse_pos):
                    print("clicked button")
                    dice_rolled = player.roll_dice(dice_count)
                    print("dice rolled", dice_rolled)
                    button_player_init.text = str(dice_tools.sum_dice(dice_rolled))

                    # reset dice count
                    dice_count = 0
                    button_dice_number.text = str(dice_count)

                if button_dice_number.is_over(mouse_pos):
                    dice_count += 1
                    button_dice_number.text = str(dice_count)









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
        button_roll_dice.draw(surface_main, True)
        button_dice_number.draw(surface_main, True)

        # update display and draw elements
        pygame.display.flip()

    # quit game
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_main_loop()

