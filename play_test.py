from entity import Entity


player = Entity(6)

dice_list = player.roll_dice(3)
print(dice_list, int(player.dice_pool))
