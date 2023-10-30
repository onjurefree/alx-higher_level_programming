#!/usr/bin/python3
"""
These is class Rectangle with two method
"""


class Rectangle:
    """These are the attributes of this class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """This method returns width"""
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

    """This method returns hight"""
    @property
    def height(self):
        return self.__height

    """This method sets hight"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
