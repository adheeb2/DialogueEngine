class Player:
    def __init__(self):
        self.inventory = []
        self.quests = {}
        self.flags = {}
    def add_item(self, item):
        self.inventory.append(item)
        print(f"[You received:{item}]")
    def remove_item(self,item):
        self.inventory.remove(item)
        print(f"[You lost:{item}]")
    def give_quest(self,quest_name):
        self.quests[quest_name]= "active"
        print(f"[New quest:{quest_name}]")