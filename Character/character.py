import random

class Character:
    def __init__(self, name="Unnamed"):
        self.name = name
        self.stats = self.generate_stats()
        self.items = []

    def generate_stats(self):
        return {
            "HP": int(50 + 50 * random.random()),
            "ATK": int(5 + 10 * random.random()),
            "CRIT": int(10 + 20 * random.random()),  # Critical hit chance
            "DODGE": int(10 + 20 * random.random())  # Dodge chance
        }

    def take_damage(self, damage):
        self.stats["HP"] = max(0, self.stats["HP"] - damage)

    def dodge_attack(self, dodge_chance_modifier):
        dodge_chance = int(100 * random.random())
        dodge_value = self.stats.get("DODGE", 0)  
        return dodge_chance <= dodge_value + dodge_chance_modifier

    def critical_attack(self, crit_chance_modifier):
        critical_chance = int(100 * random.random())
        crit_value = self.stats.get("CRIT", 0) 
        return critical_chance <= crit_value + crit_chance_modifier

