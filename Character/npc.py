from Character.character import Character
import random
class NPC(Character):
    def __init__(self):
        super().__init__()
        self.characteristic = random.choice(["gentle", "rude", "neutral"])

    
    def choose_attack(self):
        pass

    def taunt_player(self):
        taunts = {
            "gentle": [
                "You fight bravely, but this is not your day.",
                "A valiant effort, but you should surrender.",
                "You have skill, but I must prevail.",
                "Your heart is strong, but so is my blade.",
                "This battle will end peacefully—for me.",
            ],
            "rude": [
                "You think you can defeat me?",
                "Prepare to lose!",
                "Is that all you've got?",
                "I'll crush you like an insect!",
                "You're pathetic, even for a challenge!",
            ],
            "neutral": [
                "Let us see who is stronger.",
                "A good fight is what I live for!",
                "This will be a battle to remember.",
                "Strength meets strength today.",
                "May the best fighter win!",
            ],
        }
        characteristic_taunt =  taunts.get(self.characteristic, taunts["neutral"])
        return random.choice(characteristic_taunt)
    
    

