import random

def attack(attacker, defender):
    critical_hit = calculate_critical_hit(attacker)
    damage = attacker.stats["ATK"] * (2 if critical_hit else 1)
    defender.take_damage(damage)
    return critical_hit

def calculate_critical_hit(attacker):
    return random.random() < 0.1  # 10% chance for a critical hit

def start_combat(player, npc):
    round_number = 1
    while player.stats["HP"] > 0 and npc.stats["HP"] > 0:
        print(f"\n--- Round {round_number} ---")
        print(f"{player.name}'s turn:")
        if not player.dodge_attack():
            critical = attack(player, npc)
            print(f"{npc.name} takes {'critical ' if critical else ''}damage!")
        else:
            print(f"{npc.name}'s attack missed!")

        if npc.stats["HP"] <= 0:
            print(f"{npc.name} has been defeated!")
            return player

        print(f"{npc.name}'s turn:")
        npc.taunt_player()
        if not player.dodge_attack():
            critical = attack(npc, player)
            print(f"{player.name} takes {'critical ' if critical else ''}damage!")
        else:
            print(f"{player.name}'s attack missed!")

        if player.stats["HP"] <= 0:
            print(f"{player.name} has been defeated!")
            return npc

        round_number += 1

def check_victory(player, npc):
    if player.stats["HP"] > 0 and npc.stats["HP"] <= 0:
        return f"{player.name} wins!"
    elif npc.stats["HP"] > 0 and player.stats["HP"] <= 0:
        return f"{npc.name} wins!"
    else:
        return "It's a draw!"
