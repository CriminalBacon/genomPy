# 3rd party modules
import tcod as libtcod
import pygame
import random

# game file

import constants
import gui_elements
from entity import Entity
import dice_tools
import engine


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
    engine.random_turn(npc)

    # initialize dice count
    dice_count = 0

    # initialize game state
    game_quit = False
    engine.reset_stance(player, npc)

    # creates text boxes for hp, initiative, attack, defence
    button_player_hp = gui_elements.Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 200,
                                           50, 25)
    button_npc_hp = gui_elements.Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 200, 50, 25)

    button_player_init = gui_elements.Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 250,
                                           50, 25)
    button_npc_init = gui_elements.Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 250, 50, 25)
    button_player_attack = gui_elements.Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 300,
                                           50, 25)
    button_npc_attack = gui_elements.Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 300, 50, 25)
    button_player_defence = gui_elements.Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 350,
                                           50, 25)
    button_npc_defence = gui_elements.Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 350, 50, 25)

    button_roll_dice = gui_elements.Button(constants.COLOR_CYAN, constants.PLAYER_X + 175, constants.PLAYER_Y + 400,
                                           100, 50, "Roll")
    button_dice_number = gui_elements.Button(constants.COLOR_GOLD, constants.PLAYER_X + 100, constants.PLAYER_Y + 400,
                                             40, 40)
    button_dice_pool = gui_elements.Button(constants.COLOR_MAGENTA, constants.PLAYER_X + 25, constants.PLAYER_Y + 400,
                                             40, 40)

    button_next_turn = gui_elements.Button(constants.COLOR_RED, constants.PLAYER_X + 325, constants.PLAYER_Y + 400,
                                           40, 40, ">")

    button_debug = gui_elements.Button(constants.COLOR_WHITE, 0, 0, 300, 40)


    while not game_quit:

        # set hp
        button_player_hp.text = str(player.hp)
        button_npc_hp.text = str(npc.hp)
        button_dice_pool.text = str(player.dice_pool)

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            # process input
            if event.type == pygame.QUIT:
                game_quit = True
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if button_roll_dice.is_over(mouse_pos):

                    if player.stance == 'init':
                        dice_rolled = player.roll_dice(dice_count)
                        print("dice rolled", dice_rolled)
                        player.init = dice_tools.sum_dice(dice_rolled)
                        button_player_init.text = str(player.init)
                        button_npc_init.text = str(npc.init)

                        engine.roll_for_initiative(player, npc)

                        # update dice pool
                        player.dice_pool -= dice_count
                        # reset dice count
                        dice_count = 0
                        button_dice_number.text = str(dice_count)
                        break

                    if player.stance == 'attack':
                        dice_rolled = player.roll_dice(dice_count)
                        print("dice rolled", dice_rolled)
                        player.attack = dice_tools.sum_dice(dice_rolled)
                        button_player_attack.text = str(player.attack)
                        button_npc_defence.text = str(npc.defence)
                        engine.roll_for_attack(player, npc)

                        # update dice pool
                        player.dice_pool -= dice_count
                        # reset dice count
                        dice_count = 0
                        button_dice_number.text = str(dice_count)
                        player.has_attacked = True
                        break

                    if player.stance == 'defence':
                        dice_rolled = player.roll_dice(dice_count)
                        print("dice rolled", dice_rolled)
                        player.defence = dice_tools.sum_dice(dice_rolled)
                        button_player_defence.text = str(player.defence)
                        button_npc_attack.text = str(npc.attack)

                        engine.roll_for_attack(npc, player)


                        # update dice pool
                        player.dice_pool -= dice_count
                        # reset dice count
                        dice_count = 0
                        button_dice_number.text = str(dice_count)
                        player.has_defended = True
                        break

                if button_dice_number.is_over(mouse_pos):
                    dice_count += 1
                    button_dice_number.text = str(dice_count)

                if button_next_turn.is_over(mouse_pos):
                    # reset game state
                    engine.reset_stance(player, npc)

                    button_player_init.text = str('')
                    button_npc_init.text = str('')

                    button_player_attack.text = str('')
                    button_npc_attack.text = str('')

                    button_player_defence.text = str('')
                    button_npc_defence.text = str('')

                    # reset dice pool to max dice pool
                    player.dice_pool = player.max_dice_pool

                    button_dice_number.text = str('')

                    engine.random_turn(npc)

                if player.has_attacked and not player.has_defended:
                    player.stance = 'defence'
                elif not player.has_attacked and player.has_defended:
                    player.stance = 'attack'




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
        button_dice_pool.draw(surface_main, True)

        if player.has_attacked and player.has_defended:
            button_next_turn.draw(surface_main, True)

        # #### debug button #####
        button_debug.text = str(player.has_attacked) + ' '  + str(player.has_defended) + ' ' + player.stance
        button_debug.draw(surface_main)
        # ####              #####
        # update display and draw elements
        pygame.display.flip()

    # quit game
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_main_loop()

