import os

from mcdreforged.api.all import *


psi = ServerInterface.psi()
mcdr_permission = "permission.yml"
server_folder = psi.get_mcdr_config().get('working_directory')
config_folder = psi.get_data_folder()
config_file = os.path.join(config_folder, 'config.yml')
usercache_file = os.path.join(server_folder, 'usercache.json')
floodgate_config_file = os.path.join(server_folder, "plugins", "floodgate", "config.yml")