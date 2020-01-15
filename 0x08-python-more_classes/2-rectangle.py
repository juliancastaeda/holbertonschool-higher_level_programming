#!/usr/bin/python3
"""
   create
   the new
   class
"""


class Rectangle():
    def __init__(self, width=0, height=0):

        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return ((self.__width + self.__height) * 2)
