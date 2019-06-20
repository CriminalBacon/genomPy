import random
from dice_tools import sum_dice


class Entity:
    def __init__(self, dice_pool):
        self.dice_pool = dice_pool
        self.max_dice_pool = dice_pool
        self.hp = 20
        self.init = 0
        self.attack = 0
        self.defence = 0
        self.goes_first = False
        self.is_dead = False
        self.has_attacked = False
        self.has_defended = False
        self.stance = ''

    def roll_dice(self, number_to_roll):
        roll_list = []
# FIXME took out check to test gui
#       if number_to_roll <= self.dice_pool:
#           self.dice_pool -= number_to_roll

        for x in range(number_to_roll):
            roll_list.append(random.randint(1, 6))

        return roll_list

    def set_init(self, rolled_init):
        self.init = sum_dice(rolled_init)

    def set_attack(self, rolled_attack):
        self.attack = sum_dice(rolled_attack)

    def set_defence(self, rolled_defence):
        self.defence = sum_dice(rolled_defence)

    def take_damage(self, x):
        self.hp -= x
        self.check_for_death()

    def check_for_death(self):
        if self.hp < 0:
            self.is_dead = True

    def print_stats(self):
        print("HP = {0} Init = {1}   Atk = {2}   Def = {3}".format(self.hp, self.init, self.attack, self.defence))

    def reset(self):
        self.dice_pool = self.max_dice_pool

