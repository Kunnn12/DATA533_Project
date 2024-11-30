import random
class Player:
    def __init__(self):
        self.hp = int(50 + 50 * random.random())
        self.atk = int(5 + 10 * random.random())
        self.crit = 30 * random.random()
        self.dodge = 30 * random.random()

    def use_item(item):
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

tallhand = Player()
print(tallhand.hp)
tallhand.take_damage(10)
print(tallhand.hp)
tallhand.take_damage(5)
print(tallhand.hp)