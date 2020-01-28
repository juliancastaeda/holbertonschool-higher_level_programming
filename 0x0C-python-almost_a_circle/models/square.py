#!/usr/bin/python3
"""
comment
"""


from models.base import Base
from models.rectangle import Rectangle
"""
comment
"""


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Function comments"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        comment
        """
        a = 'Square'
        b = self.width
        return ("[{}] ({}) {}/{} - {}".format(a, self.id, self.x, self.y, b))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        """
        cooment
        """
        i = 0
        list = ['id', 'size', 'x', 'y']
        if len(args) > 0 and args is not None:
            for value in args:
                setattr(self, list[i], value)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
                i += 1
