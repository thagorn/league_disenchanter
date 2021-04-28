from managers.materialmanager import MaterialManager
from managers.shardmanager import ShardManager

class CraftResult:
    def __init__(self):
        self.materials = MaterialManager()
        self.shards = ShardManager()

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

    def list_gains(self):
        self.materials.list_gains()
        self.shards.list_gains()
            
