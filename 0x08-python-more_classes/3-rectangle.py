#!/usr/bin/python3
"""
This is class rectangle
The class has four methods and __str__
"""


class Rectangle:
    """These are the methods of this class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """This str method prints rectangle"""
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = ""
        for _ in range(self.__height):
            shape += "#" * self.__width + "\n"
        return shape[:-1]

    """This method returns the width"""
    @property
    def width(self):
        return self.__width

    """This method sets the width"""
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

    """This method sets height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """This method returns the area"""
    def area(self):
        return self.__width * self.__height

    """this method returns the perimeter"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.__width + self.__height)
