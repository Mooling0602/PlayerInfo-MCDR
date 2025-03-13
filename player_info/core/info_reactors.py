import copy
import re
import player_info.data as data

from mcdreforged.api.all import *
from player_info.utils import get_floodgate_player_pfx


def get_online_players(content: str, match) -> list:
    names_section = content[match.end():].strip()
    online_list = [name.strip() for name in names_section.split(",")]
    return online_list

def get_online_geyser_players(content: str, match) -> list:
    names_section = content[match.end():].strip()
    online_list = [name.strip() for name in names_section.split()]
    return online_list

@new_thread('GetOnlinePlayers')
def get_online_info(info: Info):
    data.floodgate_player_pfx = get_floodgate_player_pfx()
    match_list = re.match(r"There are \d+ of a max of \d+ players online:", info.content)
    match_geyser_list = [
        re.match(r"在线玩家 \((\d+)\):", info.content),
        re.match(r"Online Players \((\d+)\):", info.content)
    ]
    if match_list:
        data.online_player_list = get_online_players(info.content, match_list)
    for i in match_geyser_list:
        if i:
            data.online_geyser_players_list = get_online_geyser_players(info.content, i)
            break

@new_thread('ParseOnlinePlayers')
def parse_online_info():
    updated_online_players = []
    def get_player_info_element() -> dict:
        return {'name': None, 'be_client': None}
    if data.online_player_list is not None:
        for i in data.online_player_list:
            e = get_player_info_element()
            e.update(name=i, be_client=False)
            updated_online_players.append(e)
    if data.online_geyser_players_list is not None:
        for index, i in enumerate(data.online_geyser_players_list):
            if data.floodgate_player_pfx is not None:
                if data.floodgate_player_pfx + i in data.online_player_list:
                    data.online_geyser_players_list[index] = data.floodgate_player_pfx + i
        for index, p in enumerate(updated_online_players):
            if p.get('name', None) in data.online_geyser_players_list:
                p.update(be_client=True)
                updated_online_players[index] = p
    data.online_players = updated_online_players    






    