import requests

from typing import Optional
from player_info.utils import load_json_dict, get_mcdr_player_list
from player_info.paths import usercache_file


# 基于读取usercache.json结合使用ojang接口进行查询的全新方案
def get_player_uuid(player: str, online_api: Optional[bool] = None):
    usercache = load_json_dict(usercache_file)
    if not online_api:
        for i in usercache:
            # 没考虑重名情况，出问题再说~
            if i.get('name', None) == player:
                uuid = i.get('uuid', None)
                return uuid
    else:
        try:
            resp = requests.get("https://api.mojang.com/users/profiles/minecraft/" + player)
            result = resp.json()
            uuid = result["id"]
            uuid = f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
        except Exception:
            uuid = None
        return uuid
    
def match_player_name(uuid: str, online_api: Optional[bool] = None):
    if not online_api:
        if '-' not in uuid:
            uuid = f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
        usercache = load_json_dict(usercache_file)
        for i in usercache:
            if i.get('uuid', None) == uuid:
                player = i.get('name', None)
                return player
    else:
        try:
            uuid = uuid.replace('-', '')
            url = f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}'
            resp = requests.get(url)
            result = resp.json()
            player = result.get('name')
        except Exception:
            player = None
        return player
    
def is_player_member(player: str) -> bool:
    mcdr_player_list = get_mcdr_player_list()
    for i in mcdr_player_list:
        if i == player:
            return True
    return False