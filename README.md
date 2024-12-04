# DATA533_Project
# Simple Battle

**Simple Battle** is a turn-based battle simulator where players engage in combat with NPC opponents. The game features dynamic events, random stat generation, and critical hit/dodge mechanics for an engaging experience. The project is structured into two sub-packages: **Character** and **Gameplay**, each focusing on specific game elements.

---

## Package Structure

### 1. **Character Sub-Package**
Defines the characters participating in the game, including both players and NPCs. Inheritance is used to share common behavior.

#### Modules:
- **`character.py`**
  - The base `Character` class, providing shared properties and methods.
  - **Functions:**
    - `generate_stats()`: Randomly assigns stats for a character:
      - **HP (Health Points):** Range 50-100.
      - **ATK (Attack Power):** Range 5-15.
      - **CRIT (Critical Hit Chance):** Range 10-30%.
      - **DODGE (Dodge Chance):** Range 10-30%.
    - `take_damage(damage)`: Reduces the character's HP by the specified damage value. Ensures HP does not fall below 0.
    - `dodge_attack(dodge_modifier)`: Determines if the character successfully dodges an incoming attack based on dodge stats and modifiers.
    - `critical_attack(crit_modifier)`: Determines if a critical hit occurs, doubling the damage dealt.

- **`player.py`**
  - The `Player` class inherits from `Character`.
  - **Functions:**
    - `choose_attack(player_input)`: Allows the player to select an attack type (Basic, Heavy, or Quick) and returns its details:
      - **Basic Attack:** Normal damage, standard dodge/crit chance.
      - **Heavy Strike:** Higher damage, easier to dodge.
      - **Quick Attack:** Lower damage, harder to dodge, higher crit chance.

- **`npc.py`**
  - The `NPC` class inherits from `Character` and represents the non-playable opponent.
  - **Functions:**
    - `choose_attack()`: Randomly selects an attack type (Basic, Heavy, or Quick) and returns its details.
    - `taunt_player()`: Generates a random taunt based on the NPC's personality ("gentle", "rude", or "neutral").

---

### 2. **Gameplay Sub-Package**
Manages game mechanics, including random events, combat, and user interface interactions.

#### Modules:
- **`events.py`**
  - Generates random events that modify player stats.
  - **Functions:**
    - `generate_event()`: Randomly selects an event from a predefined list.
    - `apply_item_effect(player, item)`: Applies the effects of an item (e.g., boost `CRIT`, `DODGE`, or `HP`) to the player's stats.
    - `handle_event(player)`: Executes a random event, such as discovering a weapon, avoiding a trap, or training to improve stats.

- **`combat.py`**
  - Manages the turn-based combat system.
  - **Functions:**
    - `execute_player_turn(player, npc)`: Prompts the player to choose an action (Attack or Skip Turn) and processes the chosen action.
    - `execute_npc_turn(npc, player)`: Processes the NPC's turn by randomly selecting and executing an attack.
    - `start_combat(player, npc)`: Alternates turns between the player and the NPC until one is defeated, incorporating dodge and critical hit mechanics.

- **`interface.py`**
  - Handles user interaction and game display elements.
  - **Functions:**
    - `display_ascii_art(title)`: Displays ASCII art for important game events like "Victory" or "Defeat."
    - `display_stats(character)`: Displays the current stats of a character.
    - `display_combat_round(round_number, player, npc)`: Shows the combat round's details, including health bars and stats.
    - `get_player_action()`: Prompts the player to choose an action (e.g., Attack or Skip Turn).
    - `display_last_message(result)`: Displays the result of the battle with animations.

---

## Game Flow
1. **Start Screen:**
   - The game displays the title "Simple Battle" with ASCII art.
   - The player is prompted to enter their name.

2. **Random Event:**
   - A random event occurs, potentially affecting the player's stats.
   - Events include finding items, training to boost `CRIT` or `DODGE`, and avoiding traps.

3. **Combat:**
   - A turn-based combat sequence begins against an NPC.
   - The player and NPC take turns attacking until one is defeated.
   - Combat includes mechanics for dodging and critical hits.

4. **End Screen:**
   - The game declares the winner and displays a closing message.

---

## How to Play
1. Clone or download the repository.
2. Ensure all dependencies (e.g., `pyfiglet`, `colorama`) are installed:
   ```bash
   pip install pyfiglet colorama

        