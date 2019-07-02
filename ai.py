import engine


def roll_init_for_npc(npc):
    init_roll = npc.roll_dice(2)
    npc.init = engine.sum_dice(init_roll)


def roll_attack_for_npc(npc):
    attack_roll = npc.roll_dice(2)
    npc.attack = engine.sum_dice(attack_roll)


def roll_damage_for_npc(npc):
    damage_roll = npc.roll_dice(2)
    npc.damage = engine.sum_dice(damage_roll)


def roll_defence_for_npc(npc):
    defence_roll = npc.roll_dice(2)
    npc.defence = engine.sum_dice(defence_roll)