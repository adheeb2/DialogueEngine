import json
def load_dialogue_tree(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[Error] File {path} is not found")
        return {}
    except json.JSONDecodeError as e:
        print(f"[Error] Invalid Json: {e}")
        return {}
def check_condition(player,condition_str):
    if not condition_str:
        return True
    if condition_str.startswith("has_item:"):
        item = condition_str.split(":",1)[1]
        return item in player.inventory
    return False
def execute_action(player,action_str):
    actions = action_str.split(",")
    for act in actions:
         if act.startswith("give_quest:"):
             quest = act.split(":",1)[1]
             player.give_quest(quest)
         elif act.startswith("remove_item:"):
             item = act.split(":",1)[1]
             player.remove_item(item)
             
            