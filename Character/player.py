from Character.character import Character
class Player(Character):
    def __init__(self):
        super().__init__(name="Player")

    def use_item(self, item):
        effect = item.get("effect", {})
        for key, value in effect.items():
            self.stats[key] = min(self.stats.get(key, 0) + value, 100)
    
    def choose_attack(self, player_input):
        """Choose an attack based on the player's input."""
        attack_choice = ""
        damage = 0
        dodge_chance_modifier = 0
        crit_chance_modifier = 0  # Modifier for the crit chance

        # Determine the attributes for each attack type based on player's input
        if player_input == "1" or player_input.upper() == "BASIC ATTACK":
            attack_choice = "Basic Attack"
            damage = self.atk
            dodge_chance_modifier = 0  # Normal dodge chance
            crit_chance_modifier = 0  # Normal crit chance
        elif player_input == "2" or player_input.upper() == "HEAVY STRIKE":
            attack_choice = "Heavy Strike"
            damage = self.atk * 1.5  # Increased damage
            dodge_chance_modifier = 20  # Easier to dodge
            crit_chance_modifier = 0  # Normal crit chance
        elif player_input == "3" or player_input.upper() == "QUICK ATTACK":
            attack_choice = "Quick Attack"
            damage = self.atk * 0.5  # Lower damage
            dodge_chance_modifier = -20  # Harder to dodge
            crit_chance_modifier = 15  # Increased crit chance
        else:
            print("Invalid input, defaulting to Basic Attack.")
            attack_choice = "Basic Attack"
            damage = self.atk
            dodge_chance_modifier = 0
            crit_chance_modifier = 0
        
        # Return a dictionary with attack type, damage, dodge modifier, and crit chance modifier
        return {
            "attack_type": attack_choice,
            "damage": damage,
            "dodge_chance_modifier": dodge_chance_modifier,
            "crit_chance_modifier": crit_chance_modifier
        }
