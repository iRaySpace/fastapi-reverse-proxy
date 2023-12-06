import yaml

_config = None

def init_config():
    global _config
    if _config is None:
        with open("config.yaml", "r") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            _config = config


def get_config(key):
    return _config.get(key, None)

