from Character.player import Player
from Character.npc import NPC
from Gameplay.combat import start_combat
from Gameplay.events import handle_event
from Gameplay.interface import (
    display_ascii_art, display_stats, display_last_message
)

def main():
    # 显示启动画面
    display_ascii_art("start")
    print("Welcome to the RPG Turn-Based Game!")

    # 初始化玩家和NPC
    player_name = input("Enter your character's name: ").strip()
    player = Player()
    player.name = player_name

    npc = NPC()
    npc.name = "Goblin"

    # 事件阶段
    print("\nYour journey begins with a mysterious event...")
    handle_event(player)

    # 显示初始状态
    print("\nHere are your stats after the event:")
    display_stats(player)
    print("\nA wild Goblin appears to challenge you!")
    display_stats(npc)

    # 战斗阶段
    print("\nThe battle begins!")
    start_combat(player, npc)

    # 确定胜者
    winner = player.name if player.stats["HP"] > 0 else npc.name
    result_message = f"The winner is {winner}!"
    display_ascii_art("win" if winner == player.name else "lose")
    display_last_message(result_message)

    # 游戏结束提示
    print("\nThanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
