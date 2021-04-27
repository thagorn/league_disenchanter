from responses.recipe import Recipe
from util.apiaccessor import ApiAccessor

class MaterialManager:
    def __init__(self):
        self.api_accessor = ApiAccessor()
        self.orange = 0
        self.blue = 0
        self.key_fragments = 0
        self.keys = 0
        self.gemstones = 0
        self.key_chests = []
        self.keyless_chests = []
        self.chest_counts = [0, 0, 0, 0]

    def process(self, item):
        if item["lootId"] == "CURRENCY_cosmetic":
            self.orange = item["count"]
        elif item["lootId"] == "CURRENCY_champion":
            self.blue = item["count"]
        elif item["lootId"] == "MATERIAL_key_fragment":
            self.key_fragments = item["count"]
        elif item["lootId"] == "MATERIAL_key":
            self.keys = item["count"]
        elif item["lootId"] == "MATERIAL_rare":
            self.gemstones = item["count"]
        elif item["type"] == "CHEST":
            recipe = Recipe(self.api_accessor.get_recipe_data(item["lootId"]))
            requires_key = recipe.requires_key()
            if requires_key:
                self.key_chests.append(item)
                self.chest_counts[0] += 1
                self.chest_counts[1] += item["count"]
            else:
                self.keyless_chests.append(item)
                self.chest_counts[2] += 1
                self.chest_counts[3] += item["count"]

    def print(self):
        print(f"You have {self.blue} blue essence.")
        print(f"You have {self.orange} orange essence.")
        print(f"You have {self.keys} keys and {self.key_fragments} key fragments.")
        print(f"You have {self.chest_counts[1]} chests across {self.chest_counts[0]} types that require keys.")
        print(f"You have {self.chest_counts[3]} 'chests' across {self.chest_counts[2]} types that don't require keys.")
        print(f"You have {self.gemstones} gemstones.")
