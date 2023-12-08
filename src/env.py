import pathlib
from functools import lru_cache  # hmm
from decouple import Config, RepositoryEnv

BASE_DIR = pathlib.Path(__file__).parent.parent # root folder
print(BASE_DIR)
ENV_PATH = BASE_DIR / ".env"   # the .env file 
print(ENV_PATH)

# If .env file exists, load it
@lru_cache
def get_config():
    # this function returns another function (config-func) to be called
    if ENV_PATH.exists:
        print("ENV PATH Exists")
        return Config(RepositoryEnv(str(ENV_PATH)))
    from decouple import config
    return config

config = get_config()