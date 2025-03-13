import mutils.tr as tr
import player_info.data as data

from mcdreforged.api.all import *
from player_info.core.info_reactors import get_online_info, parse_online_info
from .commands import register_command
from .config import default_config


def on_load(server: PluginServerInterface, prev_module):
    data.config = server.load_config_simple(file_name='config.yml', default_config=default_config, echo_in_console=False)
    server.logger.info(tr(server, "config.loaded"))
    register_command(server)
    if server.is_server_startup():
        on_server_startup(server)

def on_server_startup(server: PluginServerInterface):
    commands = ["list", "geyser list"]
    for i in commands:
        server.execute(i)

def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    commands = ["list", "geyser list"]
    for i in commands:
        server.execute(i)

def on_player_left(server: PluginServerInterface, player: str):
    commands = ["list", "geyser list"]
    for i in commands:
        server.execute(i)

def on_info(server: PluginServerInterface, info: Info):
    get_online_info(info)
    parse_online_info()