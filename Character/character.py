import random

class Character:
    def __init__(self):
        # HP: 50 - 100
        self.hp = int(50 + 50 * random.random())
        # ATK: 5 - 15
        self.atk = int(5 + 10 * random.random())
        # CRIT: 0% - 30% 
        self.crit = int(30 * random.random())
        # DODGE: 0% - 30% 
        self.dodge = 60 - self.crit


    def take_damage(self, amount):
        self.hp -= amount
        return self.hp

    def dodge_attack(self):
        dodge_chance = 100 * random.random()
        if dodge_chance <= self.dodge:
            return True
        else:
            return False