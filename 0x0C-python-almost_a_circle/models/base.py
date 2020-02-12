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
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ 
        comment
        """
        clas = cls.__name__
        if clas == "Rectangle":
            a = cls(23, 48)
        elif clas == "Square":
            a = cls(46)
        a.update(**dictionary)
        return(a)
    
    @classmethod
    def load_from_file(cls):
        """ 
        comment
        """
        list1 = []
        name = cls.__name__+'.json'
        try:
            with open(name, 'r') as f:
                b = cls.from_json_string(f.read())
                list1 = [cls.create(**line) for line in b]
                return list1
        except OSError:
            return (list1)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ 
        comment
        """
        list2 = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                list2.append(list_objs[i].to_dictionary())
        doc = cls.__name__+'.csv'
        with open(doc, 'w') as file:
            file.write(cls.to_json_string(list2))

    @classmethod
    def load_from_file_csv(cls):
        """ 
        comment
        """
        list3 = []
        name = cls.__name__+'.csv'
        try:
            with open(name, 'r') as f:
                x = cls.from_json_string(f.read())
                list4 = [cls.create(**line) for line in x]
                return list4
        except:
            return (list3)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        comment
        """
        color = ["blue", "green", "red"]
        for i in list_rectangles:
            y = turtle.Turtle()
            y.pencolor(random(color))
            y.visible(False)
            y.forward(15)
            var.left(25)
        
