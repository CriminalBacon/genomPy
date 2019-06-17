import random


def roll_dice(dice_pool, to_roll):
    roll_list = []
    for x in range(to_roll):
        roll_list.append(random.randint(1, 6))

    return roll_list


def total_dice(dice_to_sum):
    total = 0

    for i in dice_to_sum:
        print(i, end=' ')
        total += i

    return total


def play_turn(dice_pool, active_turn):
    print("Dice pool: {0}".format(dice_pool))
    roll = input("{0} roll: ".format(active_turn))
    


player_dice_pool = 6
init_roll = input("Initiative roll: ")
player_dice_pool -= int(init_roll)
init_total = total_dice(roll_dice(player_dice_pool, int(init_roll)))
print("\nInit: {0}".format(init_total))

print('\nDice pool: {0}'.format(player_dice_pool))
attack_roll = input("Attack roll: ")
player_dice_pool -= int(attack_roll)
attack_roll = total_dice(roll_dice(player_dice_pool, int(attack_roll)))
print("\nAttack: {0}".format(attack_roll))

print('\nDice pool: {0}'.format(player_dice_pool))


# roll = input("how many to roll: ")
# rolls = roll_dice(dp, int(roll))
#

