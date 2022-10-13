import os
from typing import Optional
from dotenv import load_dotenv
from os.path import join
from pathlib import Path

import src.core.repositories as scr
import src.config as c
from src.core.entities import EnvItemEntity


class ConfigRepo(scr.BaseRepository):
    _DOTENV_PATH = join(Path(__file__).parent.parent.parent, '.env')

    def __init__(self, dot_env_path: str = _DOTENV_PATH):
        self.dot_env_path = dot_env_path
        load_dotenv(self.dot_env_path)

    def get_one(self, key: str) -> EnvItemEntity:
        env_value = os.environ.get(key)
        env_item_entity = EnvItemEntity(key=key, value=env_value)
        return env_item_entity
