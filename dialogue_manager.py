import json
from utils import load_dialogue_tree, check_condition, execute_action

class DialogueManager:
    def __init__(self, json_path, player):
        self.tree = load_dialogue_tree(json_path)
        self.player = player
        self.npc_name = self.tree["npc"]["name"]

    def start(self):
        print(f"\n👋 You approach {self.npc_name}...\n")
        current_id = self.tree["npc"]["start_node"]

        while current_id:
            node = self.tree["nodes"].get(current_id)
            if not node:
                print(f"[Error]: Node '{current_id}' not found.")
                break

            # Branch: condition node
            if "condition" in node:
                current_id = self._handle_condition(node)
                continue

            # Branch: dialogue node
            self._display_text(node)

            if node.get("is_end"):
                break

            options = node.get("options", [])
            self._display_options(options)
            current_id = self._handle_choice(options)

        print(f"\n💬 Conversation ended.\n")

    # -----------------------
    # Internal helper methods
    # -----------------------
    def _handle_condition(self, node):
        """Handles nodes that only check conditions and route elsewhere."""
        if check_condition(self.player, node["condition"]):
            return node.get("true_next")
        return node.get("false_next")

    def _display_text(self, node):
        """Show NPC dialogue text."""
        print(f"{self.npc_name}: {node['text']}")

    def _display_options(self, options):
        """Show dialogue options."""
        for i, option in enumerate(options):
            print(f"  {i+1}. {option['text']}")

    def _handle_choice(self, options):
        """Ask player for input and return the next node ID."""
        try:
            choice = int(input(" → ")) - 1
            if 0 <= choice < len(options):
                selected = options[choice]

                # Execute any actions attached to the option
                if "action" in selected:
                    execute_action(self.player, selected["action"])

                return selected.get("next")

            print("⚠️ Invalid choice.")
        except ValueError:
            print("⚠️ Please enter a number.")

        return None  # fallback if input fails
