from managers.materialmanager import MaterialManager
from managers.shardmanager import ShardManager

class CraftResult:
    def __init__(self):
        self.materials = MaterialManager()
        self.shards = ShardManager()
        self.disenchanted_champions = 0
        self.disenchanted_skins = 0
        self.disenchanted_wardskins = 0
        self.disenchanted_eternals = 0
        self.disenchanted_icons = 0

    def _count_cost(self, item, reduction):
        if item["type"] == "CHAMPION_RENTAL":
            self.disenchanted_champions += reduction
        elif item["type"] == "SKIN_RENTAL":
            self.disenchanted_skins += reduction
        elif item["type"] == "WARDSKIN_RENTAL":
            self.disenchanted_wardskins += reduction
        elif item["type"] == "STATSTONE_SHARD":
            self.disenchanted_eternals += reduction
        elif item["type"] == "SUMMONERICON":
            self.disenchanted_icons += reduction

    def add_result(self, result_data):
        added_data = result_data["added"]
        for entry in added_data:
            additional = entry["deltaCount"]
            item = entry["playerLoot"]
            if item["type"] == "CHAMPION_RENTAL":
                self.shards.increment(item, additional)
            elif item["type"] == "SKIN_RENTAL":
                self.shards.increment(item, additional)
            elif item["type"] == "WARDSKIN_RENTAL":
                self.shards.increment(item, additional)
            elif item["type"] == "STATSTONE_SHARD":
                self.shards.increment(item, additional)
            elif item["type"] == "SUMMONERICON":
                self.shards.increment(item, additional)
            elif item["type"] == "CURRENCY":
                self.materials.increment(item, additional)
            elif item["type"] == "MATERIAL":
                self.materials.increment(item, additional)
            elif item["type"] == "CHEST":
                self.materials.increment(item, additional)
        removed_data = result_data["removed"]
        for entry in removed_data:
            reduction = entry["deltaCount"]
            item = entry["playerLoot"]
            self._count_cost(item, reduction)

    def list_gains(self):
        self.materials.list_gains()
        self.shards.list_gains()

    def list_disenchanting_costs(self):
        c = f"{self.disenchanted_champions} champion shards" if self.disenchanted_champions > 0 else None
        s = f"{self.disenchanted_skins} skin shards" if self.disenchanted_skins > 0 else None
        w = f"{self.disenchanted_wardskins} ward skin shards" if self.disenchanted_wardskins > 0 else None
        e = f"{self.disenchanted_eternals} eternals" if self.disenchanted_eternals > 0 else None
        i = f"{self.disenchanted_icons} icons" if self.disenchanted_icons > 0 else None
        costs = ", ".join(cost for cost in[c, s, w, e, i] if cost)
        print(f"After disenchanting {costs}:")
