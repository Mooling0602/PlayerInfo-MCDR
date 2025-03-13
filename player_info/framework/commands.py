import player_info.data as data

from mcdreforged.api.all import *
from player_info.core.query import query_profile
from player_info.utils import get_mcdr_player_list, check_uuid_valid


builder = SimpleCommandBuilder()

@builder.command('!!list')
def on_list_online(src: CommandSource, ctx: CommandContext):
    src.reply("------ Online Players ------")
    for i in data.online_players:
        if i.get('name', None) is not None and i.get('name', None) != "":
            be_client = i.get('be_client', None)
            if be_client is True:
                is_be = "[BEClient]"
            else:
                is_be = ''
            src.reply(f"- {is_be}{i.get('name', None)}")

@builder.command('!!list debug result')
def print_list_online_result(src: CommandSource, ctx: CommandContext):
    print(data.online_players)

@builder.command('!!list debug all')
def print_list_online_all(src: CommandSource, ctx: CommandContext):
    print(data.online_player_list)

@builder.command('!!list debug geyser')
def print_list_online_geyser(src: CommandSource, ctx: CommandContext):
    print(data.online_geyser_players_list)

@builder.command('!!pinfo list members')
def on_list_players(src: CommandSource, ctx: CommandContext):
    src.reply("Player members in this server:")
    for i in get_mcdr_player_list():
        src.reply(f"- {i}")

@builder.command('!!pinfo query <uuid|player_name>')
def on_query(src: CommandSource, ctx: CommandContext):
    arg = ctx['uuid|player_name']
    for i in query_profile(arg):
        src.reply(i)

@builder.command('!!pinfo query <uuid|player_name> --get-uuid')
def on_query_uuid(src: CommandSource, ctx: CommandContext):
    arg = ctx['uuid|player_name']
    if check_uuid_valid(arg) is True:
        raise IllegalArgument('Need a player_name!', 15)
    result = query_profile(arg, "uuid")
    i = result[0] if result is not None else None
    if result is not None:
        src.reply(i)
    else:
        src.reply('No result.')

@builder.command('!!pinfo query <uuid|player_name> --get-name')
def on_query_name(src: CommandSource, ctx: CommandContext):
    arg = ctx['uuid|player_name']
    if check_uuid_valid(arg) is False:
        raise IllegalArgument('Need a UUID!', 15)
    result = query_profile(arg, "player")
    i = result[0] if result is not None else None
    if result is not None:
        src.reply(i)
    else:
        src.reply('No result.')

def register_command(server: PluginServerInterface):
    builder.arg('uuid|player_name', Text)
    builder.register(server)

