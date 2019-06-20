import pygame
import constants


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
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


def create_button_dictionary():
    dict_button = {}

    dict_button["button_player_hp"] = Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 200,
                                           50, 25)
    dict_button["button_npc_hp"] = Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 200, 50, 25)

    dict_button["button_player_init"] = Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 250,
                                           50, 25)
    dict_button["button_npc_init"] = Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 250, 50, 25)

    dict_button["button_player_attack"] = Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 300,
                                           50, 25)
    dict_button["button_npc_attack"] = Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 300, 50, 25)

    dict_button["button_player_defence"] = Button(constants.COLOR_WHITE, constants.PLAYER_X + 100, constants.PLAYER_Y + 350,
                                           50, 25)
    dict_button["button_npc_defence"] = Button(constants.COLOR_WHITE, constants.NPC_X + 100, constants.NPC_Y + 350, 50, 25)

    dict_button["button_roll_dice"] = Button(constants.COLOR_CYAN, constants.PLAYER_X + 175, constants.PLAYER_Y + 400,
                                           100, 50, "Roll")
    dict_button["button_dice_number"] = Button(constants.COLOR_GOLD, constants.PLAYER_X + 100, constants.PLAYER_Y + 400,
                                             40, 40)
    dict_button["button_dice_pool"] = Button(constants.COLOR_MAGENTA, constants.PLAYER_X + 25, constants.PLAYER_Y + 400,
                                             40, 40)
    dict_button["button_next_turn"] = Button(constants.COLOR_RED, constants.PLAYER_X + 325, constants.PLAYER_Y + 400,
                                           40, 40, ">")
    dict_button["button_debug"] = Button(constants.COLOR_WHITE, 0, 0, 300, 40)

    return dict_button
