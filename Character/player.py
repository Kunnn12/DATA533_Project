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

        # 改进输入解析
        player_input = player_input.strip().lower()

        if player_input in ["1", "basic attack"]:
            attack_choice = "Basic Attack"
            damage = self.atk
            dodge_chance_modifier = 0
            crit_chance_modifier = 0
        elif player_input in ["2", "heavy strike"]:
            attack_choice = "Heavy Strike"
            damage = self.atk * 1.5
            dodge_chance_modifier = 20  # Easier to dodge
            crit_chance_modifier = 0
        elif player_input in ["3", "quick attack"]:
            attack_choice = "Quick Attack"
            damage = self.atk * 0.5
            dodge_chance_modifier = -20  # Harder to dodge
            crit_chance_modifier = 15
        else:
            print("Invalid input, defaulting to Basic Attack.")
            attack_choice = "Basic Attack"
            damage = self.atk
            dodge_chance_modifier = 0
            crit_chance_modifier = 0

        return {
            "attack_type": attack_choice,
            "damage": damage,
            "dodge_chance_modifier": dodge_chance_modifier,
            "crit_chance_modifier": crit_chance_modifier
        }

