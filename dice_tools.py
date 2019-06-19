# def dice_turn(entity):
#     #print("Dice pool: {0}".format(entity.dice_pool))
#     #roll_count = input("Roll: ")
#     dice = entity.roll_dice(int(roll_count))
#     print_dice_list(dice)
#     #print("Total: {0}\n".format(sum_dice(dice)))
#     return dice



def sum_dice(dice_list):
    total = 0

    for i in dice_list:
        total += i

    return total


def print_dice_list(dice_list):
    for i in dice_list:
        print(i, end=' ')





