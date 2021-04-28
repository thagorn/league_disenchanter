import requests
from util.config import Config

import json

class ApiAccessor:
    def __init__(self):
        self.config = Config()
        self.api_base = "/lol-loot/v1"

    def _get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'Basic ' + self.config.get_token()}

    def _make_get_request(self, url):
        verify = not self.config.should_disable_certificate_check()
        if verify:
            verify = self.config.get_root_certificate_location()
        return requests.get(url, headers=self._get_headers(), verify=verify)

    def _make_post_request(self, url, data):
        verify = not self.config.should_disable_certificate_check()
        if verify:
            verify = self.config.get_root_certificate_location()
        return requests.post(url, json=data, headers=self._get_headers(), verify=verify)
    
    def _get_api_url(self):
        return self.config.get_base_url() + self.api_base

    def get_recipe_data(self, item_id):
        url = self._get_api_url() + "/recipes/initial-item/" + item_id
        return self._make_get_request(url).json()

    def get_loot_data(self):
        url = self._get_api_url() + "/player-loot"
        return self._make_get_request(url).json()

    def disenchant_champion_shard(self, loot_id, number):
        #url = self._get_api_url() + f"/recipes/CHAMPION_RENTAL_disenchant/craft?repeat={number}"
        #data = [loot_id]
        #returnval = self._make_post_request(url, data).json()
        with open("output.json", "r") as jsonfile:
            returnval = json.load(jsonfile)
        return returnval
