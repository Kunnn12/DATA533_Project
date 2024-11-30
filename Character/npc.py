import random
class Npc:
    def __init__(self):
        self.hp = int(50 + 50 * random.random())
        self.atk = int(5 + 10 * random.random())
        self.crit = 30 * random.random()
        self.dodge = 30 * random.random()

    def choose_attack(self):
        pass

    def take_damage(self, amount):
        self.hp -= amount
        return self.hp

    def dodge_attack(self):
        dodge_chance = 100 * random.random()
        if dodge_chance <= self.dodge:
            return True
        else:
            return False

    def taunt_player():
        pass

npc = Npc()
print(npc.hp)