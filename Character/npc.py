from Character.character import Character
import random
class NPC(Character):
    def __init__(self):
        super().__init__(name="Enemy")
        self.characteristic = random.choice(["gentle", "rude", "neutral"])

    
    def choose_attack(self):
        attacks = ["Basic Attack", "Heavy Strike", "Quick Attack"]
        chosen_attack = random.choice(attacks)

        if chosen_attack == "Basic Attack":
            attack_choice = "Basic Attack"
            damage = self.atk
            dodge_chance_modifier = 0  # Normal dodge chance
            crit_chance_modifier = 0  # Normal crit chance
        elif chosen_attack == "Heavy Strike":
            attack_choice = "Heavy Strike"
            damage = self.atk * 1.5  # Increased damage
            dodge_chance_modifier = 20  # Easier to dodge
            crit_chance_modifier = 0  # Normal crit chance
        else:
            attack_choice = "Quick Attack"
            damage = self.atk * 0.5  # Lower damage
            dodge_chance_modifier = -20  # Harder to dodge
            crit_chance_modifier = 15  # Increased crit chance
        
        return {
            "attack_type": attack_choice,
            "damage": damage,
            "dodge_chance_modifier": dodge_chance_modifier,
            "crit_chance_modifier": crit_chance_modifier
        }

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
    
    

