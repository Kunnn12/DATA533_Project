# Gameplay/combat.py
from Character.player import Player
from Character.npc import NPC

def get_player_input():
    """Function to get the player's input for the attack."""
    print("Choose your attack:")
    print("1: Basic Attack")
    print("2: Heavy Strike")
    print("3: Quick Attack")
    return input("Enter the number of your choice: ")

def start_combat():
    """Starts the combat between the player and the NPC."""
    # Create NPC and player instances
    npc = NPC()
    player = Player()

    # Main combat loop
    while player.hp > 0 and npc.hp > 0:
        # Get player input and pass it to choose_attack
        player_input = get_player_input()
        player_attack = player.choose_attack(player_input)
        print(f"Player chooses {player_attack['attack_type']}!")

        # Check if NPC dodges orm
        #  takes damage
        if npc.dodge_attack(player_attack["dodge_chance_modifier"]):
            print("NPC dodges the attack!")
        else:
            if player.critical_attack(player_attack["crit_chance_modifier"]):
                npc.take_damage(player_attack["damage"] * 2)  # Critical hit
                print("Player CRIT!")
            else:
                npc.take_damage(player_attack["damage"])
            print(f"NPC's HP: {npc.hp}")

        # NPC's turn (implement NPC behavior)
        # For simplicity, you can make NPC also choose randomly or use any logic
        npc_attack = npc.choose_attack()  # Assuming NPC has a similar method
        print(f"NPC chooses {npc_attack['attack_type']}!")

        # Simulate NPC's attack
        if player.dodge_attack(npc_attack["dodge_chance_modifier"]):
            print("Player dodges the attack!")
        else:
            if npc.critical_attack(npc_attack["crit_chance_modifier"]):
                player.take_damage(npc.atk * 2)  # Critical hit
                print("NPC CRIT!")
            else:
                player.take_damage(npc.atk)
            print(f"Player's HP: {player.hp}")

    print("The battle is over!")
