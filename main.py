from player import Player
from dialogue_manager import DialogueManager

def main():
    player = Player()
    print("NPC Dialogue System - Phase 1")
    print("Commands: talk to hermit, give_amulet, status, quit")

    while True:
        cmd = input("\n> ").strip().lower()

        if cmd == "quit":
            print("👋 Goodbye.")
            break

        elif cmd == "talk to hermit":
            dm = DialogueManager("data/hermit.json", player)
            dm.start()

        elif cmd == "give_amulet":
            player.add_item("amulet_of_light")

        elif cmd == "status":
            print(f"🎒 Inventory: {player.inventory}")
            print(f"📜 Quests: {player.quests}")

        else:
            print("⚠️ Unknown command. Options: talk to hermit, give_amulet, status, quit")

if __name__ == "__main__":
    main()
