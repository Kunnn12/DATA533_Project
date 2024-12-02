import random

class NPC:
    def __init__(self, name):
        self.name = name
        self.stats = self.generate_stats()

    def generate_stats(self):
        return {
            "HP": random.randint(70, 100),
            "ATK": random.randint(8, 18),
            "DEF": random.randint(3, 12)
        }

    def choose_attack(self):
        return random.choice(["Basic Attack", "Heavy Strike", "Quick Jab"])

    def take_damage(self, amount):
        damage = max(0, amount - self.stats["DEF"])
        self.stats["HP"] = max(0, self.stats["HP"] - damage)

    def taunt_player(self):
        taunts = [
            "You think you can defeat me?",
            "Prepare to lose!",
            "Is that all you've got?"
        ]
        print(random.choice(taunts))
