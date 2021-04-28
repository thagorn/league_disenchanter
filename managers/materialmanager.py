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
        self.chestmap = {}

    def _requires_key(self, chest):
        chest_id = chest["lootId"]
        if chest_id in self.chestmap:
            return self.chestmap[chest_id]
        recipe = Recipe(self.api_accessor.get_recipe_data(chest_id))
        requires_key = recipe.requires_key()
        self.chestmap[chest_id] = requires_key
        return requires_key

    def increment(self, item, count):
        if item["lootId"] == "CURRENCY_cosmetic":
            self.orange += count
        elif item["lootId"] == "CURRENCY_champion":
            self.blue += count
        elif item["lootId"] == "MATERIAL_key_fragment":
            self.key_fragments += count
        elif item["lootId"] == "MATERIAL_key":
            self.keys+= count
        elif item["lootId"] == "MATERIAL_rare":
            self.gemstones += count
        elif item["type"] == "CHEST":
            requires_key = self._requires_key(item)
            if requires_key:
                self.key_chests.append(item)
                self.chest_counts[0] += 1
                self.chest_counts[1] += item["count"]
            else:
                self.keyless_chests.append(item)
                self.chest_counts[2] += 1
                self.chest_counts[3] += item["count"]

    def process(self, item):
        self.increment(item, item["count"])

    def summarize(self):
        self._output("have")

    def list_gains(self):
        self._output("gained")

    def _output(self, keyword):
        if self.blue > 0:
            print(f"You {keyword} {self.blue} blue essence.")
        if self.orange > 0:
            print(f"You {keyword} {self.orange} orange essence.")
        if (self.keys > 0) or (self.key_fragments > 0):
            print(f"You {keyword} {self.keys} keys and {self.key_fragments} key fragments.")
        if self.chest_counts[1] > 0:
            print(f"You {keyword} {self.chest_counts[1]} chests across {self.chest_counts[0]} types that require keys.")
        if self.chest_counts[3] > 0:
            print(f"You {keyword} {self.chest_counts[3]} 'chests' across {self.chest_counts[2]} types that don't require keys.")
        if self.gemstones > 0:
            print(f"You {keyword} {self.gemstones} gemstones.")
