from typing import Optional
from player_info.utils import check_uuid_valid
from .id import match_player_name, get_player_uuid, is_player_member

def query_profile(text_arg: str, specify: Optional[str] = None) -> list:
    result = []
    uuid = None
    player = None
    if check_uuid_valid(text_arg) is True:
        uuid = text_arg
    else:
        player = text_arg
    result.append('------ Player Profile ------')
    if uuid:
        player = match_player_name(uuid)
        if player is None:
            player = match_player_name(uuid, True)
        if specify == "player":
            return [player]
    if player:
        uuid = get_player_uuid(player)
        if uuid is None:
            uuid = get_player_uuid(uuid, True)
        if specify == "uuid":
            return [uuid]
    if specify is None:
        result.append(f'- Name: {player}')
        result.append(f'- UUID: {uuid}')
        result.append(f'- Is member: {is_player_member(player)}')
        return result