#!/usr/bin/python3
"""
comment
"""


import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function comments"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        comment
        """
        if len(list_dictionaries) < 0 and list_dictionaries is None:
            return '"[]"'
        else:
            return json.dumps(list_dictionaries)
