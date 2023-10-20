import json

def get_path(key):
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config.get(key, None)