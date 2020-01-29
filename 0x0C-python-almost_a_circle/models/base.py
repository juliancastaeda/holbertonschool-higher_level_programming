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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        comment
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        comment
        """
        list_ = []
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs is not None:
                for i in list_objs:
                    list_.append(i.to_dictionary())
            file.write(cls.to_json_string(list_))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return ''
        else:
            return json.loads(json_string)
