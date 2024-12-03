from Character.player import Player
from Character.npc import NPC
from Gameplay.combat import start_combat, check_victory
from Gameplay.interface import (
    display_event_description, display_stats, display_combat_round,
    get_player_action, display_player_action_result, display_last_message,
    display_visual_health_bar, display_ascii_art
)

def main():
    # ASCII Art for the start of the game
    display_ascii_art("start")
    print("Welcome to the RPG Turn-Based Game!")

    # Initialize player and NPC
    player_name = input("Enter your character's name: ")
    player = Player(name=player_name)
    npc = NPC(name="Goblin")

    print("\nA wild Goblin appears!")
    display_stats(player)
    display_stats(npc)

    # Start Combat
    print("\nThe battle begins!")
    round_number = 1
    while player.stats["HP"] > 0 and npc.stats["HP"] > 0:
        display_combat_round(round_number, player, npc)
        display_visual_health_bar(player.name, player.stats["HP"], 100)
        display_visual_health_bar(npc.name, npc.stats["HP"], 100)

        # Player chooses an action
        action = get_player_action()
        display_player_action_result(action)

        # Simple attack action for demonstration
        if action == "1":
            npc.stats["HP"] -= 10
        elif action == "2":
            player.stats["HP"] += 5
        elif action == "3":
            print("You skipped your turn!")

        # NPC attacks
        player.stats["HP"] -= 8
        round_number += 1

    # Display final result
    result = check_victory(player, npc)
    display_ascii_art("win" if result.startswith(player.name) else "lose")
    display_last_message(result)

if __name__ == "__main__":
    main()
