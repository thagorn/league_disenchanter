class Recipe:
    def __init__(self, recipe_json):
        self.recipe_json = recipe_json

    def requires_key(self):
        first_recipe = self.recipe_json[0]
        for slot in first_recipe["slots"]:
            for loot_id in slot["lootIds"]:
                if loot_id == "MATERIAL_key":
                    return True
        return False

