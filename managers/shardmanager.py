from util.config import Config

class ChampionShardManager:
    def __init__(self, minimum):
        self.minimum = minimum
        self.shards = []
        self.blue_available = 0
        self.disenchant_count = 0

    def increment(self, shard, count):
        self.shards.append(shard)
        self.blue_available += shard["disenchantValue"] * count
        self.disenchant_count += count

    def process(self, shard):
        self.shards.append(shard)
        extra = shard["count"] - self.minimum
        if extra > 0:
            self.blue_available += shard["disenchantValue"] * extra
            self.disenchant_count += extra

    def list_gains(self):
        if len(self.shards) == 0:
            return
        print(f"You gained champion shards for {len(self.shards)} champions.")
        print(f"If you disenchanted all of these shards you would disenchant " \
              f"{self.disenchant_count} shards and receive " \
              f"{self.blue_available:,} blue essence.")

    def summarize(self):
        if len(self.shards) == 0:
            return
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

    def increment(self, shard, count):
        self.shards.append(shard)
        self.orange_available += shard["disenchantValue"] * count
        self.disenchant_count += count

    def process(self, shard):
        self.shards.append(shard)
        if self.disenchant_owned and shard["itemStatus"] == "OWNED":
            extra = shard["count"]
        else:
            extra = shard["count"] - self.minimum
        if extra > 0:
            self.orange_available += shard["disenchantValue"] * extra
            self.disenchant_count += extra

    def list_gains(self, name):
        if len(self.shards) == 0:
            return
        plural = "" if len(self.shards) == 1 else "s"
        print(f"You gained {len(self.shards)} unique {name}{plural}.")
        print(f"If you disenchanted all of these shards you would disenchant " \
              f"{self.disenchant_count} shards and receive " \
              f"{self.orange_available:,} orange essence.")

    def summarize(self, name):
        if len(self.shards) == 0:
            return
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

    def increment(self, shard, count):
        if shard["type"] == "CHAMPION_RENTAL":
            self.champions.increment(shard)
        elif shard["type"] == "SKIN_RENTAL":
            self.skins.increment(shard)
        elif shard["type"] == "WARDSKIN_RENTAL":
            self.wardskins.increment(shard)
        elif shard["type"] == "STATSTONE_SHARD":
            self.eternals.increment(shard)
        elif shard["type"] == "SUMMONERICON":
            self.icons.increment(shard)

    def load(self, shard):
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

    def list_gains(self):
        self.champions.list_gains()
        self.skins.list_gains("skin shard")
        self.wardskins.list_gains("ward skin shard")
        self.eternals.list_gains("eternal")
        self.icons.list_gains("icon")

    def summarize(self):
        self.champions.summarize()
        self.skins.summarize("skin shard")
        self.wardskins.summarize("ward skin shard")
        self.eternals.summarize("eternal")
        self.icons.summarize("icon")
