import argparse
from util.apiaccessor import ApiAccessor
from responses.craftresult import CraftResult
from responses.lootinventory import LootInventory

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''\
        Manage League of Legends loot
        ____________________________

Note: This requires you to be logged into your League of Legends client
See config.json for configuration settings or README.md for additional help

Available loot manager actions:
    summarize: list contents of current inventory
    disenchant: disenchant all champion shards, skin shard, eternals and icons above the configured minimums''')
parser.add_argument('action', choices=['summarize', 'disenchant'])

def summarize_inventory():
    api_accessor = ApiAccessor()
    loot_inventory = LootInventory(api_accessor.get_loot_data())
    loot_inventory.summarize()

def disenchant_extras():
    api_accessor = ApiAccessor()
    loot_inventory = LootInventory(api_accessor.get_loot_data())
    crafting_result = CraftResult()
    disenchant_results = loot_inventory.disenchant_extras()
    for result in disenchant_results:
        crafting_result.add_result(result)
    crafting_result.list_disenchanting_costs()
    crafting_result.list_gains()
        
def run():
    args = parser.parse_args()
    if args.action == 'summarize':
        summarize_inventory()
    elif args.action == 'disenchant':
        disenchant_extras()

if __name__ == '__main__':
    run()
