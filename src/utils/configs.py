import json
from enum import Enum
from pathlib import Path
from folder_paths import base_path, get_filename_list

CUSTOM_NODES_PATH = Path(f"{base_path}/custom_nodes")

class Config(Enum):
   QUALITY = "quality.cfg"

def get_config_path(name):
    custom_nodes_paths = list(map(lambda path: Path(path), get_filename_list("custom_nodes")))
    config_path = list(filter(lambda path: name in path.name, custom_nodes_paths))
    return CUSTOM_NODES_PATH / config_path[0]

def get_config_list(name):
    with open(get_config_path(name.value)) as file:
        values = json.load(file)
        names = list(map(lambda cfg: cfg['name'], values))
        return names
    
def get_config_obj(name, config_name):
    with open(get_config_path(name.value)) as file:
        values = json.load(file)
        obj = list(filter(lambda cfg: cfg['name'] == config_name, values))[0]
        return obj
