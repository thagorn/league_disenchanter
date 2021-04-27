from util.apiaccessor import ApiAccessor
from responses.lootinventory import LootInventory
        
def run():
    api_accessor = ApiAccessor()
    loot_inventory = LootInventory(api_accessor.get_loot_data())
    loot_inventory.print()

if __name__ == '__main__':
    run()
