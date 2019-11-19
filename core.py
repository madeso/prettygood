#!/usr/bin/env python3

import os


def file_exist(file: str) -> bool:
    return os.path.isfile(file)


def get_home_folder() -> str:
    return os.path.expanduser('~')
