import dice_tools
import random

from entity import Entity


def random_turn(entity):
    roll_init = random.randint(0, entity.dice_pool)
    entity.set_init(entity.roll_dice(roll_init))
    roll_attack = random.randint(0, entity.dice_pool)
    entity.set_attack(entity.roll_dice(roll_attack))
    roll_defence = random.randint(0, entity.dice_pool)
    entity.set_defence(entity.roll_dice(roll_defence))


player = Entity(6)
npc = Entity(6)
random_turn(npc)

while not player.is_dead or not npc.is_dead:
    print("Initiative")
    player.set_init(dice_tools.dice_turn(player))
    print("Attack")
    player.set_attack(dice_tools.dice_turn(player))
    print("Defence")
    player.set_defence(dice_tools.dice_turn(player))

    if player.init >= npc.init:
        player.goes_first = True
    else:
        npc.goes_first = True

    if player.goes_first:
        if player.attack > npc.defence:
            npc.take_damage(player.attack - npc.defence)
            if npc.is_dead:
                print("npc dead")
                break
        if npc.attack > player.defence:
            player.take_damage(npc.attack - player.defence)
            if player.is_dead:
                print("player dead")
                break

    else:
        if npc.attack > player.defence:
            player.take_damage(npc.attack - player.defence)
            if player.is_dead:
                print("player dead")
                break
        if player.attack > npc.defence:
            npc.take_damage(player.attack - npc.defence)
            if npc.is_dead:
                print("npc dead")
                break

    player.print_stats()
    npc.print_stats()

    player.reset()
    npc.reset()
    random_turn(npc)




