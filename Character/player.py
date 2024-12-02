import random

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = self.generate_stats()
        self.items = []

    def generate_stats(self):
        return {
            "HP": random.randint(80, 120),
            "ATK": random.randint(10, 20),
            "DEF": random.randint(5, 15)
        }

    def use_item(self, item):
        effect = item.get("effect", {})
        for key, value in effect.items():
            self.stats[key] = min(self.stats.get(key, 0) + value, 100)

    def take_damage(self, amount):
        damage = max(0, amount - self.stats["DEF"])
        self.stats["HP"] = max(0, self.stats["HP"] - damage)

    def dodge_attack(self):
        return random.random() < 0.2  # 20% chance to dodge