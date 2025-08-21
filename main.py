import json
with open("data/hermit.json", "r") as f:
    data = json.load(f)
npc = data["npc"]
nodes = data["nodes"]
current = npc["start_node"]


while True:
    node = nodes[current]
    print("\n" + node["text"])
    if node.get("is_end"):
        break
    for i, option in enumerate(node["options"]):
         print(f"{i+1}. {option['text']}")
    while True:
        try:
            choice = int(input(">"))-1
            if 0 <=choice <len(node["options"]):
                break
            else:
                print("invalid choice, Try again")
        except ValueError:
            print("add only numbers")
    selected = node["options"][choice]
    current = selected["next"]