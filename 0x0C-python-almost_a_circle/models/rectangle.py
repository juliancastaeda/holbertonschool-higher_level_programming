#!/usr/bin/python3
"""
comment
"""


from models.base import Base
"""
comment
"""


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """function coments"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        cooment
        """
        return(self.__width * self.__height)

    def display(self):
        """
        cooment
        """
        w = self.__width
        e = self.__height
        print(self.__y * '\n' + (' ' * self.__x + '#' * w + '\n') * (e))

    def __str__(self):
        """
        cooment
        """
        h = self.__height
        r = '[Rectangle]'
        i = self.__width
        id_ = self.id
        p = self.__x
        return('{} ({}) {}/{} - {}/{}'.format(r, id_, p, self.__y, i, h))

    def update(self, *args, **kwargs):
        """
        cooment
        """
        i = 0
        list = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for value in args:
                setattr(self, list[i], value)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
                i += 1
