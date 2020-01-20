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
