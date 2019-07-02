import constants
import ai


def process_init(player, npc):
    init_roll = player.roll_dice(player.dice_number_to_roll)
    player.init = sum_dice(init_roll)

    ai.roll_init_for_npc(npc)

    if player.init >= npc.init:
        player.turn.extend(constants.ATTACK_FIRST)
        npc.turn.extend(constants.DEFEND_FIRST)
    else:
        player.turn.extend(constants.DEFEND_FIRST)
        npc.turn.extend(constants.ATTACK_FIRST)

    player.turn.remove('init')
    npc.turn.remove('init')

    player.reset_current_roll()
    npc.reset_current_roll()


def process_attack(attacker, defender):
    attack_roll = attacker.roll_dice(attacker.dice_number_to_roll)
    attacker.attack = sum_dice(attack_roll)

    ai.roll_defence_for_npc(defender)

    if attacker.attack < defender.defence:
        attacker.turn.remove('damage')

    attacker.turn.remove('attack')
    defender.turn.remove('defence')

    attacker.reset_current_roll()
    defender.reset_current_roll()


def process_damage(attacker, defender):
    damage_roll = attacker.roll_dice(attacker.dice_number_to_roll)
    attacker.damage = sum_dice(damage_roll)

    defender.take_damage(attacker.damage)

    attacker.turn.remove('damage')

    attacker.reset_current_roll()
    defender.reset_current_roll()


def process_defence(defender, attacker):
    defence_roll = defender.roll_dice(defender.dice_number_to_roll)
    defender.defence = sum_dice(defence_roll)

    ai.roll_attack_for_npc(attacker)

    if attacker.attack >= defender.defence:
        process_damage(attacker, defender)

    else:
        # skip the damage turn if attack is not high enough
        attacker.turn.remove('damage')

    attacker.turn.remove('attack')
    defender.turn.remove('defence')

    attacker.reset_current_roll()
    defender.reset_current_roll()


def process_turn(player, npc):

    if len(player.turn) > 0:
        if player.turn[0] == 'init':
            process_init(player, npc)

        elif player.turn[0] == 'attack':
            process_attack(player, npc)

        elif player.turn[0] == 'damage':
            process_damage(player, npc)

        elif player.turn[0] == 'defence':
            process_defence(player, npc)

    else:
        player.finished_turn = True
        npc.finished_turn = True


def sum_dice(dice_list):
    total = 0

    for i in dice_list:
        total += i

    return total


def print_dice_list(dice_list):
    for i in dice_list:
        print(i, end=' ')



















# import random
#
#
# def roll_for_initiative(player, npc):
#     if player.init >= npc.init:
#         player.stance = 'attack'
#         npc.stance = 'defence'
#         player.goes_first = True
#         npc.goes_first = False
#     else:
#         player.stance = 'defence'
#         npc.stance = 'attack'
#         npc.goes_first = True
#         player.goes_first = False
#
#
# def reset_stance(player, npc):
#     player.stance = 'init'
#     player.goes_first = False
#     npc.goes_first = False
#
#     player.has_attacked = False
#     player.has_defended = False
#
#     player.init = 0
#     player.attack = 0
#     player.defence = 0
#
#
# def roll_for_attack(attacking_entity, defending_entity):
#     if attacking_entity.attack > defending_entity.defence:
#         attacking_entity.rolls_for_damage = True
#         attacking_entity.stance = 'damage'
#
#
# def random_turn(entity):
#     # roll_init
#     roll_init = random.randint(0, entity.dice_pool)
#
#     # decrement dice pool
#     entity.dice_pool -= roll_init
#
#     # set init for random roll
#     entity.set_init(entity.roll_dice(roll_init))
#
#     # roll attack
#     roll_attack = random.randint(0, entity.dice_pool)
#
#     # decrement dice pool
#     entity.dice_pool -= roll_attack
#
#     # set attack for random roll
#     entity.set_attack(entity.roll_dice(roll_attack))
#
#     # roll defence
#     roll_defence = random.randint(0, entity.dice_pool)
#
#     # decrement dice pool
#     entity.dice_pool -= roll_defence
#
#     # set defence for random roll
#     entity.set_defence(entity.roll_dice(roll_defence))
#
#     entity.print_stats()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import dice_tools
# # import random
# #
# # from entity import Entity
# #
# #
# # def random_turn(entity):
# #     roll_init = random.randint(0, entity.dice_pool)
# #     entity.set_init(entity.roll_dice(roll_init))
# #     roll_attack = random.randint(0, entity.dice_pool)
# #     entity.set_attack(entity.roll_dice(roll_attack))
# #     roll_defence = random.randint(0, entity.dice_pool)
# #     entity.set_defence(entity.roll_dice(roll_defence))
# #
# #
# # player = Entity(6)
# # npc = Entity(6)
# # random_turn(npc)
# #
# # while not player.is_dead or not npc.is_dead:
# #     print("Initiative")
# #     player.set_init(dice_tools.dice_turn(player))
# #     print("Attack")
# #     player.set_attack(dice_tools.dice_turn(player))
# #     print("Defence")
# #     player.set_defence(dice_tools.dice_turn(player))
# #
# #     if player.init >= npc.init:
# #         player.goes_first = True
# #     else:
# #         npc.goes_first = True
# #
# #     if player.goes_first:
# #         if player.attack > npc.defence:
# #             npc.take_damage(player.attack - npc.defence)
# #             if npc.is_dead:
# #                 print("npc dead")
# #                 break
# #         if npc.attack > player.defence:
# #             player.take_damage(npc.attack - player.defence)
# #             if player.is_dead:
# #                 print("player dead")
# #                 break
# #
# #     else:
# #         if npc.attack > player.defence:
# #             player.take_damage(npc.attack - player.defence)
# #             if player.is_dead:
# #                 print("player dead")
# #                 break
# #         if player.attack > npc.defence:
# #             npc.take_damage(player.attack - npc.defence)
# #             if npc.is_dead:
# #                 print("npc dead")
# #                 break
# #
# #     player.print_stats()
# #     npc.print_stats()
# #
# #     player.reset()
# #     npc.reset()
# #     random_turn(npc)
# #
# #
# #
# #
