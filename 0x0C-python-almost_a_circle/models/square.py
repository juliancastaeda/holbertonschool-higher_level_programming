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
        a = '__class__.__name__'
        b = 'self.width'
        return "[{}] ({}) {}/{} - {}".format(a, self.id, self.x, self.y, b)
