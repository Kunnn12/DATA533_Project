from Character.player import Player
from Character.npc import NPC
from Gameplay.combat import start_combat
from Gameplay.events import handle_event
from Gameplay.interface import (
    display_ascii_art, display_stats, display_last_message, get_player_action
)

def main():
    display_ascii_art("start")
    print("Welcome to Simple Battle!")  

    player_name = input("Enter your character's name: ").strip()
    player = Player()
    player.name = player_name

    npc = NPC()
    npc.name = "Goblin"

    print("\nYour journey begins with a mysterious event...")
    handle_event(player)

    print("\nHere are your stats after the event:")
    display_stats(player)
    print("\nA wild Goblin appears to challenge you!")
    display_stats(npc)

    print("\nThe battle begins!")
    start_combat(player, npc)

    winner = player.name if player.stats["HP"] > 0 else npc.name
    result_message = f"The winner is {winner}!"
    display_ascii_art("win" if winner == player.name else "lose")
    display_last_message(result_message)

    print("\nThanks for playing Simple Battle! Goodbye!")  

if __name__ == "__main__":
    main()

    


