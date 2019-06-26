# modules
import sys
import tcod as libtcod
import pygame

# game files
import constants
import gui_elements
from entity import Entity
import dice_tools
import engine


def draw_headers(surface):

    # HP
    text_init_player_header = GAME_FONT.render('INIT', True, constants.COLOR_GREEN)
    text_init_npc_header = GAME_FONT.render('INIT', True, constants.COLOR_GREEN)
    surface.blit(text_init_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 200))
    surface.blit(text_init_npc_header, (constants.NPC_X, constants.NPC_Y + 200))

    # INIT
    text_atk_player_header = GAME_FONT.render('ATK', True, constants.COLOR_GREEN)
    text_atk_npc_header = GAME_FONT.render('ATK', True, constants.COLOR_GREEN)
    surface.blit(text_atk_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 250))
    surface.blit(text_atk_npc_header, (constants.NPC_X, constants.NPC_Y + 250))

    # ATTACK
    text_dmg_player_header = GAME_FONT.render('DMG', True, constants.COLOR_GREEN)
    text_dmg_npc_header = GAME_FONT.render('DMG', True, constants.COLOR_GREEN)
    surface.blit(text_dmg_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 300))
    surface.blit(text_dmg_npc_header, (constants.NPC_X, constants.NPC_Y + 300))

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

    # create dictionary of gui elements
    dict_button = gui_elements.create_button_dictionary()

    while not game_quit:

        # set hp
        # button_player_hp.text = str(player.hp)
        dict_button["button_player_hp"].text = str(player.hp)
        dict_button["button_npc_hp"].text = str(npc.hp)
        # button_npc_hp.text = str(npc.hp)
        dict_button["button_dice_pool"].text = str(player.dice_pool)



        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            # process input
            if event.type == pygame.QUIT:
                game_quit = True

            if event.type == pygame.MOUSEBUTTONDOWN:

                if dict_button["button_roll_dice"].is_over(mouse_pos):

                    if player.stance == 'init':
                        dice_rolled = player.roll_dice(dice_count)
                        print("dice rolled", dice_rolled)
                        player.init = dice_tools.sum_dice(dice_rolled)
                        dict_button["button_player_init"].text = str(player.init)
                        dict_button["button_npc_init"].text = str(npc.init)

                        engine.roll_for_initiative(player, npc)

                        # update dice pool
                        player.dice_pool -= dice_count
                        # reset dice count
                        dice_count = 0
                        dict_button["button_dice_number"].text = str(dice_count)
                        break

                    if player.stance == 'attack':
                        dice_rolled = player.roll_dice(dice_count)
                        print("dice rolled", dice_rolled)
                        player.attack = dice_tools.sum_dice(dice_rolled)
                        dict_button["button_player_attack"].text = str(player.attack)
                        dict_button["button_npc_defence"].text = str(npc.defence)
                        engine.roll_for_attack(player, npc)

                        # update dice pool
                        player.dice_pool -= dice_count
                        # reset dice count
                        dice_count = 0
                        dict_button["button_dice_number"].text = str(dice_count)
                        player.has_attacked = True
                        break

                    if player.stance == 'defence':
                        dice_rolled = player.roll_dice(dice_count)
                        print("dice rolled", dice_rolled)
                        player.defence = dice_tools.sum_dice(dice_rolled)
                        dict_button["button_player_defence"].text = str(player.defence)
                        dict_button["button_npc_attack"].text = str(npc.attack)

                        engine.roll_for_attack(npc, player)


                        # update dice pool
                        player.dice_pool -= dice_count
                        # reset dice count
                        dice_count = 0
                        dict_button["button_dice_number"].text = str(dice_count)
                        player.has_defended = True
                        break

                if dict_button["button_dice_number"].is_over(mouse_pos):
                    dice_count += 1
                    dict_button["button_dice_number"].text = str(dice_count)

                if dict_button["button_next_turn"].is_over(mouse_pos):
                    # reset game state
                    engine.reset_stance(player, npc)

                    dict_button["button_player_init"].text = str('')
                    dict_button["button_npc_init"].text = str('')

                    dict_button["button_player_attack"].text = str('')
                    dict_button["button_npc_attack"].text = str('')

                    dict_button["button_player_defence"].text = str('')
                    dict_button["button_npc_defence"].text = str('')

                    # reset dice pool to max dice pool
                    player.dice_pool = player.max_dice_pool
                    npc.dice_pool = npc.max_dice_pool

                    dict_button["button_dice_number"].text = str('')

                    # reset button color
                    for x in dict_button:
                        dict_button[x].set_original_color()

                    engine.random_turn(npc)

                if player.has_attacked and not player.has_defended:
                    player.stance = 'defence'
                elif not player.has_attacked and player.has_defended:
                    player.stance = 'attack'




        # draw game

        draw_game(surface_main, player, npc)

        # highlight which box is being rolled for
        if player.stance == 'attack':
            dict_button["button_player_attack"].set_color(constants.COLOR_LIGHT_YELLOW)
            dict_button["button_player_defence"].set_original_color()

        if player.stance == 'defence':
            dict_button["button_player_defence"].set_color(constants.COLOR_LIGHT_YELLOW)
            dict_button["button_player_attack"].set_original_color()


        for x in dict_button:
            if x != "button_next_turn":
                dict_button[x].draw(surface_main, True)

        if player.has_attacked and player.has_defended:
            dict_button["button_next_turn"].draw(surface_main, True)

        # #### debug button #####
        # button_debug.text = str(player.has_attacked) + ' ' + str(player.has_defended) + ' ' + player.stance
        # button_debug.draw(surface_main)
        # ####              #####


        # update display and draw elements
        pygame.display.flip()

    # quit game
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    game_main_loop()

