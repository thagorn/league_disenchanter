from util.config import Config

class ChampionShardManager:
    def __init__(self, minimum):
        self.minimum = minimum
        self.shards = []
        self.blue_available = 0
        self.disenchant_count = 0

    def process(self, shard):
        self.shards.append(shard)
        extra = shard["count"] - self.minimum
        if extra > 0:
            self.blue_available += shard["disenchantValue"] * extra
            self.disenchant_count += extra

    def print(self):
        print(f"You have champion shards for {len(self.shards)} champions.")
        print(f"If you disenchanted any extras above a minimum of {self.minimum} " \
              f"you would disenchant {self.disenchant_count} shards and receive " \
              f"{self.blue_available:,} blue essence.")

class SkinShardManager:
    def __init__(self, minimum, disenchant_owned):
        self.minimum = minimum
        self.disenchant_owned = disenchant_owned
        self.shards = []
        self.orange_available = 0
        self.disenchant_count = 0

    def process(self, shard):
        self.shards.append(shard)
        if self.disenchant_owned and shard["itemStatus"] == "OWNED":
            extra = shard["count"]
        else:
            extra = shard["count"] - self.minimum
        if extra > 0:
            self.orange_available += shard["disenchantValue"] * extra
            self.disenchant_count += extra

    def print(self, name):
        plural = "" if len(self.shards) == 1 else "s"
        print(f"You have {len(self.shards)} unique {name}{plural}.")
        print(f"If you disenchanted any extras above a minimum of {self.minimum} " \
              f"you would disenchant {self.disenchant_count} and receive " \
              f"{self.orange_available:,} orange essence.")

class ShardManager:
    def __init__(self):
        config = Config()
        disenchant_owned = config.should_disenchant_owned_skins()
        self.champions = ChampionShardManager(config.get_minimum_champ_shards())
        self.skins = SkinShardManager(config.get_minimum_skin_shards(), disenchant_owned)
        self.wardskins = SkinShardManager(config.get_minimum_wardskin_shards(), disenchant_owned)
        self.eternals = SkinShardManager(config.get_minimum_eternals(), disenchant_owned)
        self.icons = SkinShardManager(config.get_minimum_icons(), disenchant_owned)

    def process(self, shard):
        if shard["type"] == "CHAMPION_RENTAL":
            self.champions.process(shard)
        elif shard["type"] == "SKIN_RENTAL":
            self.skins.process(shard)
        elif shard["type"] == "WARDSKIN_RENTAL":
            self.wardskins.process(shard)
        elif shard["type"] == "STATSTONE_SHARD":
            self.eternals.process(shard)
        elif shard["type"] == "SUMMONERICON":
            self.icons.process(shard)

    def print(self):
        print("Champion shards:")
        self.champions.print()
        print("Skin shards:")
        self.skins.print("skin shard")
        print("Ward Skin shards:")
        self.wardskins.print("ward skin shard")
        print("Eternals:")
        self.eternals.print("eternal")
        print("Icons:")
        self.icons.print("icon")
