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
            "CRIT": int(30 * random.random()),
            "DODGE": int(30 * random.random())
        }

    def take_damage(self, damage):
        self.stats["HP"] = max(0, self.stats["HP"] - damage)

    def dodge_attack(self, dodge_chance_modifier):
        dodge_chance = int(100 * random.random())
        if dodge_chance <= self.stats["DODGE"] + dodge_chance_modifier:
            return True
        else:
            return False
        
    def critical_attack(self, crit_chance_modifier):
        critical_chance = int(100 * random.random())
        if critical_chance <= self.stats["DODGE"] + crit_chance_modifier:
            return True
        else:
            return False