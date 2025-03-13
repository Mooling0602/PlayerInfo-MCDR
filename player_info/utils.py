import json
import yaml
import os
import re

from player_info.paths import mcdr_permission, floodgate_config_file


def load_json_dict(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def load_yml_dict(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data

def check_uuid_valid(uuid: str) -> bool:
    uuid_regex = re.compile(
        r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    )
    return bool(uuid_regex.match(uuid))

def get_mcdr_player_list() -> list:
    mcdr_players = load_yml_dict(mcdr_permission)
    mcdr_player_list = []
    for i in mcdr_players.values():
        if isinstance(i, list):
            for sub_i in i:
                mcdr_player_list.append(sub_i)
    return mcdr_player_list

def get_floodgate_player_pfx() -> str|None:
    if os.path.exists(floodgate_config_file):
        floodgate_config = load_yml_dict(floodgate_config_file)
    else:
        floodgate_config = {}
    username_prefix = floodgate_config.get('username-prefix', None)
    if username_prefix == '':
        username_prefix = None
    return username_prefix