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


def draw_game(surface, entity_player, entity_npc):

    # clear surface
    surface.fill(constants.COLOR_DEFAULT_BG)

    # draw character
    surface.blit(constants.STICK_PLAYER, (constants.PLAYER_X, constants.PLAYER_Y) )
    surface.blit(constants.STICK_NPC, (constants.NPC_X, constants.NPC_Y))

    # draw headers
    #gui_elements.draw_headers(surface)


def game_main_loop():
    ''' In this function, we loop the main game '''

    # init pygame
    pygame.init()

    surface_main = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))

    player = Entity(6)
    npc = Entity(6)

    # initialize game state
    game_quit = False
    player.reset_turn()
    npc.reset_turn()

    # create dictionary of gui elements
    dict_button = gui_elements.create_button_dictionary(player, npc)

    while not game_quit:

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            # process input
            if event.type == pygame.QUIT:
                game_quit = True

            if event.type == pygame.MOUSEBUTTONDOWN:

                if dict_button["button_roll_dice"].is_over(mouse_pos):

                    player.dice_number_to_roll = int(dict_button["button_dice_number"].text)
                    engine.process_turn(player, npc)

                    # reset dice number to 0
                    player.dice_number_to_roll = 0

                if dict_button["button_dice_number"].is_over(mouse_pos):
                    player.dice_number_to_roll += 1
                    dict_button["button_dice_number"].text = str(player.dice_number_to_roll)

                if dict_button["button_next_turn"].is_over(mouse_pos):
                    # reset game state
                    player.reset_turn()
                    npc.reset_turn()

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

        # draw game

        draw_game(surface_main, player, npc)

        # check to see if turn is over
        if len(player.turn) == 0:
            player.turn.append("next round")
            player.finished_turn = True
            npc.finished_turn = True

        # update text boxes
        dict_button = gui_elements.update_button_dictionary(dict_button, player, npc)

        for x in dict_button:
            if x != "button_next_turn":
                dict_button[x].draw(surface_main, True)

        if player.finished_turn and npc.finished_turn:
            dict_button["button_next_turn"].draw(surface_main, True)

        # #### debug button #####
        # dict_button['button_debug'].text = str(player.turn) + str(npc.turn)
        # dict_button['button_debug'].draw(surface_main)
        # ####              #####

        # update display and draw elements

        pygame.display.flip()

    # quit game
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    game_main_loop()

