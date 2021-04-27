import base64
import json
import os

class Config:
    def __init__(self):
        config_data = self._load_config_from_file()
        self.host = config_data["host"]
        self.directory = config_data["install_directory"]
        self.minimum_champ_shards = config_data["minimum_champ_shards"]
        self.minimum_skin_shards = config_data["minimum_skin_shards"]
        self.minimum_wardskin_shards = config_data["minimum_ward_skin_shards"]
        self.minimum_eternals = config_data["minimum_eternals"]
        self.minimum_icons = config_data["minimum_icons"]
        self.disenchant_owned_skins = config_data["disenchant_owned_skins"]
        self.root_certificate_location = config_data["root_certificate_location"]
        self.disable_certificate_check = config_data["disable_certificate_check"]
        (port, token) = self._load_lockfile()
        self.port = port
        self.token = token

    def _load_config_from_file(self):
        with open('config.json', 'r') as config_file:
            return json.load(config_file)

    def _load_lockfile(self):
        lockfile_location = os.path.join(self.directory, 'lockfile')
        with open(lockfile_location, 'r') as lockfile:
            [_, _, port, password, _] = lockfile.readline().split(":", 4)
        auth = "riot:" + password.strip()
        auth_bytes = auth.encode("ascii")
        auth_b64_bytes = base64.b64encode(auth_bytes)
        auth_b64_string = auth_b64_bytes.decode("ascii")
        return (port, auth_b64_string)
        
    def get_base_url(self):
        return self.host + ":" + self.port

    def get_minimum_champ_shards(self):
        return self.minimum_champ_shards
    def get_minimum_skin_shards(self):
        return self.minimum_skin_shards
    def get_minimum_wardskin_shards(self):
        return self.minimum_wardskin_shards
    def get_minimum_eternals(self):
        return self.minimum_eternals
    def get_minimum_icons(self):
        return self.minimum_icons
    def should_disenchant_owned_skins(self):
        return self.disenchant_owned_skins
    def get_token(self):
        return self.token
    def get_root_certificate_location(self):
        return self.root_certificate_location
    def should_disable_certificate_check(self):
        return self.disable_certificate_check
