import pyfiglet
from colorama import Fore, Style

def display_ascii_art(title):
    """
    Displays ASCII art for important game events using pyfiglet.
    """
    art_map = {
        "start": pyfiglet.figlet_format("RPG Game"),
        "win": pyfiglet.figlet_format("Victory!"),
        "lose": pyfiglet.figlet_format("Defeat...")
    }
    print(Fore.CYAN + art_map.get(title, "") + Style.RESET_ALL)

def display_event_description(event):
    """
    Describes the random event that occurs, providing context to the player.
    """
    print(Fore.MAGENTA + "=" * 40)
    print(f"Event: {event}")
    print("=" * 40 + Style.RESET_ALL)

def display_stats(character):
    """
    Displays the current stats of the character (Player or NPC).
    """
    print(Fore.YELLOW + "=" * 40)
    print(f"{character.name}'s Stats:")
    for key, value in character.stats.items():
        print(f"{key}: {value}")
    print("=" * 40 + Style.RESET_ALL)

def display_combat_round(round_number, player, npc):
    """
    Displays the current combat round with a simple ASCII-based UI.
    """
    print(Fore.GREEN + "-" * 40)
    print(f"Round {round_number}")
    print(f"{player.name}: {player.stats['HP']} HP")
    print(f"{npc.name}: {npc.stats['HP']} HP")
    print("-" * 40 + Style.RESET_ALL)

def get_player_action():
    """
    Prompts the player to choose an action during their turn.
    """
    print(Fore.BLUE + "\nChoose your action:")
    print("1. Attack")
    print("2. Use Item")
    print("3. Skip Turn")
    print(Style.RESET_ALL)
    action = input(Fore.LIGHTBLUE_EX + "Enter the number of your action: " + Style.RESET_ALL)
    return action

def display_player_action_result(action):
    """
    Describes the effects of the actions the player takes.
    """
    action_map = {
        "1": "You chose to attack!",
        "2": "You chose to use an item!",
        "3": "You chose to skip your turn!"
    }
    print(Fore.CYAN + action_map.get(action, "Invalid action. Try again.") + Style.RESET_ALL)

def display_last_message(result):
    """
    Displays the result of the combat.
    """
    print(Fore.RED + "=" * 40)
    print(f"Final Result: {result}")
    print("=" * 40 + Style.RESET_ALL)

def display_visual_health_bar(name, hp, max_hp):
    """
    Displays a visual health bar for a character with colors.
    """
    bar_length = 20
    filled_length = int(bar_length * hp / max_hp)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    color = Fore.RED if hp / max_hp <= 0.3 else Fore.YELLOW if hp / max_hp <= 0.6 else Fore.GREEN
    print(f"{name}: {color}[{bar}] {hp}/{max_hp} HP{Style.RESET_ALL}")

