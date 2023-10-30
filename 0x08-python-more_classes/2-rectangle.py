#!/usr/bin/python3
"""
This is class rectangle
The class has four method for width, height, area and perimeter
"""


class Rectangle:
    """these are the class attributes"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """This method returns width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    """This method returns height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """This method return the square of rectangle"""
    def area(self):
        return self.__height * self.__width

    """This method return perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__height + self.__width)
