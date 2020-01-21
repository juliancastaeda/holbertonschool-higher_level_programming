#!/usr/bin/python3
class BaseGeometry():
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.__name = name
        self.__value = value
        if type(self.__value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if self.__value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        a = '[Rectangle] '
        b = '/'
        return ("{}{}{}{}".format(a, self.__width, b, self.__height))


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
