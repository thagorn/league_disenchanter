# League Loot Manager

## How to run

1. Log into the League of Legends client
2. Run `python3 loot_manager.py`

## Config settings
Change these in config.json
  * host: ip address to connect to league client, should just be local host
  * install_directory: location of your league of legends client
  * minimum_champ_shards: number of champion shards to keep for each champion when disenchanting
  * minimum_skin_shards: number of skin shards to keep for each unique skin when disenchanting
  * minimum_ward_skin_shards: number of ward skin shards to keep for each unique ward skin when disenchanting
  * minimum_eternals: number of eternals to keep for each unique eternal when disenchanting
  * minimum_icons: number of icons to keep for each unique icon when disenchanting
  * disenchant_owned_skins: set to true if you want to disenchant any skin shards for skins you already own
  * root_certificate_location: location on disk you've downloaded the certificate for Riot's API (see below)
  * disable_certificate_check: set to true if you want to skip the certificate check instead of downloading the pem

### Getting root certificate
Download the root certificate from https://static.developer.riotgames.com/docs/lol/riotgames.pem
Set the location you've downloaded it to in config.json
OR
Set "disable_certificate_check" to true in config.json
