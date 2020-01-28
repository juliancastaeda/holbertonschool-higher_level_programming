#!/usr/bin/python3
"""
comment
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """function coments"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
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
        d = self.__y
        print(d * '\n' + (' ' * self.__x + '#' * w + '\n') * (e), end='')

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
        list = ['id', 'size', 'x', 'y']
        if len(args) > 0 and args is not None:
            for value in args:
                setattr(self, list[i], value)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
                i += 1

    def to_dictionary(self):
        """
        comment
        """
        a = self.width
        b = self.height
        c = self.id
        dict = {'x': self.x, 'y': self.y, 'id': c, 'width': a, 'height': b}
        return dict
