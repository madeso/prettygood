#!/usr/bin/env python3

from .core import *

import os
import typing
import json


def get_config_file_name(name: str) -> str:
    return os.path.join(get_home_folder(), '.' + name + '.json')


class Config:
    def __init__(self, name: str, data: typing.Dict[str, str]):
        self.name = name
        self.data = data

    def save(self):
        with open(get_config_file_name(self.name), 'w', encoding="utf-8") as f:
            print(json.dumps(self.data, sort_keys=True, indent=4), file=f)


def get_user_data(name: str) -> Config:
    if file_exist(get_config_file_name(name)):
        with open(get_config_file_name(name), 'r', encoding="utf-8") as f:
            return Config(name, json.loads(f.read()))
    else:
        return Config(name, {})


class Settings:
    def __init__(self, name, default_value):
        self.name = name
        self.default_value = default_value

    def get_value(self, config: Config):
        if self.name not in config.data:
            return self.default_value
        else:
            return config.data[self.name]

    def set_value(self, config: Config, value):
        config.data[self.name] = value

    def set_default_if_missing(self, config: Config):
        if self.name not in config.data:
            config.data[self.name] = self.default_value
