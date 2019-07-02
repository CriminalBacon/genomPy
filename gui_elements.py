import pygame
import constants


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.original_color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('New Times Roman', 32)
            text = font.render(self.text, 1, constants.COLOR_BLACK)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        # pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def set_color(self, new_color):
        self.color = new_color

    def set_original_color(self):
        self.color = self.original_color


def create_button_dictionary(player, npc):
    dict_button = {}

    dict_button["button_player_hp"] = Button(constants.COLOR_GREY, constants.PLAYER_X + 40, constants.PLAYER_Y - 40,
                                           50, 25, str(player.hp))

    dict_button["button_npc_hp"] = Button(constants.COLOR_GREY, constants.NPC_X + 40, constants.NPC_Y - 40, 50, 25,
                                          str(npc.hp))

    dict_button["button_player_init"] = Button(constants.COLOR_WHITE, constants.PLAYER_X - 30, constants.PLAYER_Y + 10,
                                           30, 25, str(player.init))

    dict_button["button_npc_init"] = Button(constants.COLOR_WHITE, constants.NPC_X + 125, constants.NPC_Y + 10, 30, 25,
                                            str(npc.init))

    dict_button["button_player_attack"] = Button(constants.COLOR_WHITE, constants.PLAYER_X - 30, constants.PLAYER_Y + 60,
                                           30, 25, str(player.attack))

    dict_button["button_npc_attack"] = Button(constants.COLOR_WHITE, constants.NPC_X + 125, constants.NPC_Y + 60, 30, 25,
                                              str(npc.attack))

    dict_button["button_player_damage"] = Button(constants.COLOR_WHITE, constants.PLAYER_X - 30, constants.PLAYER_Y + 110,
                                                 30, 25, str(player.damage))

    dict_button["button_npc_damage"] = Button(constants.COLOR_WHITE, constants.NPC_X + 125, constants.NPC_Y + 110,
                                              30, 25, str(npc.damage))

    dict_button["button_player_defence"] = Button(constants.COLOR_WHITE, constants.PLAYER_X - 30, constants.PLAYER_Y + 160,
                                           30, 25, str(player.defence))

    dict_button["button_npc_defence"] = Button(constants.COLOR_WHITE, constants.NPC_X + 125, constants.NPC_Y + 160, 30,
                                               25, str(npc.defence))

    dict_button["button_dice_pool"] = Button(constants.COLOR_MAGENTA, constants.PLAYER_X + 135, constants.PLAYER_Y + 50,
                                             40, 40, str(player.dice_pool))

    dict_button["button_dice_number"] = Button(constants.COLOR_GOLD, constants.PLAYER_X + 135, constants.PLAYER_Y + 125,
                                             40, 40, "0")

    dict_button["button_npc_dice_pool"] = Button(constants.COLOR_MAGENTA, constants.NPC_X - 60, constants.NPC_Y + 50,
                                             40, 40, str(player.dice_pool))

    dict_button["button_npc_dice_number"] = Button(constants.COLOR_GOLD, constants.NPC_X - 60, constants.NPC_Y + 125,
                                             40, 40, "0")

    dict_button["button_roll_dice"] = Button(constants.COLOR_CYAN, constants.PLAYER_X + 200, constants.PLAYER_Y + 200,
                                           100, 50, "Roll")

    dict_button["button_next_turn"] = Button(constants.COLOR_RED, constants.PLAYER_X + 301, constants.PLAYER_Y + 200,
                                           20, 50, ">")

    dict_button["button_turn_display"] = Button(constants.COLOR_WHITE, constants.PLAYER_X + 200, constants.PLAYER_Y - 100,
                                                125, 40, str(player.turn[0]))

    # dict_button["button_debug"] = Button(constants.COLOR_WHITE, 0, 0, 300, 40)

    return dict_button


def update_button_dictionary(dict_button, player, npc):
    dict_button["button_player_hp"].text = str(player.hp)
    dict_button["button_npc_hp"].text = str(npc.hp)

    dict_button["button_player_init"].text = str(player.init)
    dict_button["button_npc_init"].text = str(npc.init)

    dict_button["button_player_attack"].text = str(player.attack)
    dict_button["button_npc_attack"].text = str(npc.attack)

    dict_button["button_player_damage"].text = str(player.damage)
    dict_button["button_npc_damage"].text = str(npc.damage)

    dict_button["button_player_defence"].text = str(player.defence)
    dict_button["button_npc_defence"].text = str(npc.defence)

    dict_button["button_dice_pool"].text = str(player.dice_pool)

    dict_button["button_dice_number"].text = str(player.dice_number_to_roll)

    dict_button["button_turn_display"].text = str(player.turn[0])

    return dict_button


def draw_headers(surface):
    text_init_player_header = constants.HEADER_FONT.render('INIT', True, constants.COLOR_GREEN)
    # text_init_player_header = GAME_FONT.render('INIT', True, constants.COLOR_GREEN)
    text_init_npc_header = constants.HEADER_FONT.render('INIT', True, constants.COLOR_GREEN)
    surface.blit(text_init_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 200))
    surface.blit(text_init_npc_header, (constants.NPC_X, constants.NPC_Y + 200))

    # INIT
    text_atk_player_header = constants.HEADER_FONT.render('ATK', True, constants.COLOR_GREEN)
    text_atk_npc_header = constants.HEADER_FONT.render('ATK', True, constants.COLOR_GREEN)
    surface.blit(text_atk_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 250))
    surface.blit(text_atk_npc_header, (constants.NPC_X, constants.NPC_Y + 250))

    # ATTACK
    text_dmg_player_header = constants.HEADER_FONT.render('DMG', True, constants.COLOR_GREEN)
    text_dmg_npc_header = constants.HEADER_FONT.render('DMG', True, constants.COLOR_GREEN)
    surface.blit(text_dmg_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 300))
    surface.blit(text_dmg_npc_header, (constants.NPC_X, constants.NPC_Y + 300))

    # DEFENCE
    text_def_player_header = constants.HEADER_FONT.render('DEF', True, constants.COLOR_GREEN)
    text_def_npc_header = constants.HEADER_FONT.render('DEF', True, constants.COLOR_GREEN)
    surface.blit(text_def_player_header, (constants.PLAYER_X, constants.PLAYER_Y + 350))
    surface.blit(text_def_npc_header, (constants.NPC_X, constants.NPC_Y + 350))


