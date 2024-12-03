import random

def generate_event():
    """
    Randomly selects an event that can happen during the game.
    Events include positive and negative outcomes.
    """
    events = [
        "Find Healing Potion",
        "Discover a Weapon",
        "Encounter a Trap",
        "Meet a Merchant",
        "Mysterious Chest",
        "Ambushed by Bandits",
        "Blessing from a Sage",
        "Cursed Relic"
    ]
    return random.choice(events)

def get_item():
    """
    Randomly assigns an item to the player.
    Items have different effects, either positive or negative.
    """
    items = [
        {"name": "Healing Potion", "effect": {"HP": 20}},
        {"name": "Attack Boost", "effect": {"ATK": 5}},
        {"name": "Defense Shield", "effect": {"DEF": 5}},
        {"name": "Poison Vial", "effect": {"HP": -10}},  # Negative effect
        {"name": "Mystic Orb", "effect": {"ATK": 10, "DEF": 10}},
        {"name": "Cursed Amulet", "effect": {"HP": -20, "DEF": -5}}  # Negative effect
    ]
    return random.choice(items)

def apply_item_effect(player, item):
    """
    Applies the effects of the item to the player's stats.
    """
    effect = item.get("effect", {})
    print(f"\nYou received {item['name']}!")
    for key, value in effect.items():
        player.stats[key] = max(0, player.stats.get(key, 0) + value)  # Prevent negative stats
        print(f"{key} {'increased' if value > 0 else 'decreased'} by {abs(value)}.")
    print(f"Updated stats: {player.stats}")

def handle_event(player):
    """
    Triggers a random event and applies its effects to the player.
    """
    event = generate_event()
    print(f"\nEvent: {event}")

    if event == "Find Healing Potion":
        item = {"name": "Healing Potion", "effect": {"HP": 20}}
        apply_item_effect(player, item)

    elif event == "Discover a Weapon":
        item = {"name": "Legendary Sword", "effect": {"ATK": 15}}
        apply_item_effect(player, item)

    elif event == "Encounter a Trap":
        item = {"name": "Trap Damage", "effect": {"HP": -15}}
        apply_item_effect(player, item)

    elif event == "Meet a Merchant":
        print("You met a merchant! He offers to sell you a shield for 5 gold.")
        choice = input("Do you buy the shield? (yes/no): ").strip().lower()
        if choice == "yes":
            item = {"name": "Merchant's Shield", "effect": {"DEF": 10}}
            apply_item_effect(player, item)
        else:
            print("You walk away from the merchant.")

    elif event == "Mysterious Chest":
        print("You found a mysterious chest!")
        choice = input("Do you open it? (yes/no): ").strip().lower()
        if choice == "yes":
            # Random reward or punishment
            chest_rewards = [
                {"name": "Treasure", "effect": {"HP": 30, "ATK": 10}},
                {"name": "Poison Gas", "effect": {"HP": -20}}
            ]
            item = random.choice(chest_rewards)
            apply_item_effect(player, item)
        else:
            print("You leave the chest untouched.")

    elif event == "Ambushed by Bandits":
        print("You were ambushed by bandits! You lose some HP.")
        item = {"name": "Bandit Attack", "effect": {"HP": -25}}
        apply_item_effect(player, item)

    elif event == "Blessing from a Sage":
        print("A sage blesses you with magical energy!")
        item = {"name": "Sage's Blessing", "effect": {"HP": 20, "ATK": 10, "DEF": 10}}
        apply_item_effect(player, item)

    elif event == "Cursed Relic":
        print("You found a cursed relic! It drains your energy.")
        item = {"name": "Cursed Relic", "effect": {"HP": -15, "ATK": -5}}
        apply_item_effect(player, item)

