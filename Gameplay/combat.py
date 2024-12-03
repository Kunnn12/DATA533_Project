from Character.player import Player
from Character.npc import NPC
from Gameplay.interface import (
    display_combat_round, display_last_message, get_player_action
)

def execute_player_turn(player, npc):
    """
    Handles the player's turn: processes the player's chosen action.
    """
    action = get_player_action()

    if action == "1":  # Attack
        attack_choice = input("Choose your attack: 1. Basic Attack  2. Heavy Strike  3. Quick Attack\n")
        player_attack = player.choose_attack(attack_choice)
        print(f"{player.name} chooses {player_attack['attack_type']}!")
        if npc.dodge_attack(player_attack["dodge_chance_modifier"]):
            print(f"{npc.name} dodges the attack!")
        else:
            damage = player_attack["damage"]
            if player.critical_attack(player_attack["crit_chance_modifier"]):
                damage *= 2
                print("Critical Hit!")
            npc.take_damage(damage)
            print(f"{npc.name} takes {damage} damage. Remaining HP: {npc.stats['HP']}")

    elif action == "2":  # Skip Turn
        print(f"{player.name} skips the turn.")

def execute_npc_turn(npc, player):
    """
    Handles the NPC's turn: randomly chooses and executes an attack.
    """
    npc_attack = npc.choose_attack()
    print(f"{npc.name} chooses {npc_attack['attack_type']}!")
    if player.dodge_attack(npc_attack["dodge_chance_modifier"]):
        print(f"{player.name} dodges the attack!")
    else:
        damage = npc_attack["damage"]
        if npc.critical_attack(npc_attack["crit_chance_modifier"]):
            damage *= 2
            print("Critical Hit!")
        player.take_damage(damage)
        print(f"{player.name} takes {damage} damage. Remaining HP: {player.stats['HP']}")

def start_combat(player, npc):
    """
    Starts and manages the combat loop between the player and the NPC.
    """
    round_number = 1

    while player.stats["HP"] > 0 and npc.stats["HP"] > 0:
        print(f"\n--- Combat Round {round_number} ---")
        display_combat_round(round_number, player, npc)

        # Player's Turn
        execute_player_turn(player, npc)
        if npc.stats["HP"] <= 0:
            print(f"{npc.name} has been defeated!")
            break

        # NPC's Turn
        execute_npc_turn(npc, player)
        if player.stats["HP"] <= 0:
            print(f"{player.name} has been defeated!")
            break

        round_number += 1

    # Determine and Display Result
    winner = player.name if player.stats["HP"] > 0 else npc.name
    display_last_message(f"The winner is {winner}!")
