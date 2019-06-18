# 3rd party modules
import tcod as libtcod
import pygame

# game files
import constants


def draw_game():

    global SURFACE_MAIN

    # clear surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    # update the display
    pygame.display.flip()


def game_initialize():
    ''' This functions initializes the main window and pygame '''

    global SURFACE_MAIN

    # init pygame
    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))


def game_main_loop():
    ''' In this function, we loop the main game '''

    game_quit = False

    while not game_quit:

        # get player input
        events_list = pygame.event.get()

        # process input
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True

        # draw game
        draw_game()

    # quit game
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_initialize()
    game_main_loop()

