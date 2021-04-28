from managers.materialmanager import MaterialManager
from managers.tokenmanager import TokenManager
from managers.shardmanager import ShardManager

class LootInventory:
    def __init__(self, loot_json):
        self.other = []
        self.shards = ShardManager()
        self.materials = MaterialManager()
        self.tokens = TokenManager()
        for item in loot_json:
            self._process(item)

    def _process(self, item):
        if item["type"] == "CHAMPION_RENTAL":
            self.shards.load(item)
        elif item["type"] == "SKIN_RENTAL":
            self.shards.load(item)
        elif item["type"] == "WARDSKIN_RENTAL":
            self.shards.load(item)
        elif item["type"] == "STATSTONE_SHARD":
            self.shards.load(item)
        elif item["type"] == "SUMMONERICON":
            self.shards.load(item)
        elif item["type"] == "CURRENCY":
            self.materials.process(item)
        elif item["type"] == "MATERIAL":
            self.materials.process(item)
        elif item["type"] == "CHEST":
            self.materials.process(item)
        elif item["type"] == "CHAMPION_TOKEN":
            self.tokens.process(item)

    def disenchant_extras(self):
        return self.shards.disenchant_extras()

    def summarize(self):
        self.materials.summarize()
        self.tokens.summarize()
        self.shards.summarize()

