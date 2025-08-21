class Player:
    def __init__(self,name):
        self.name = name
        self.inventory = []
        self.quests = {}
        self.flags= {}
    def add_item(self,item):
        self.inventory.append(item)
        print(f"[You receieved:{item}] ")
    def remove_item(self,item):
        self.inventory.remove(item)
        print(f"[You lost: {item}]")
    def give_quests(self,quest_name):
        self.quests[quest_name] = "active"
        print(f"[New quest:{quest_name}]")
