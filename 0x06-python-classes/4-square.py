#!/usr/bin/python3
"""
This is class square with its attributes
"""


class Square:

    """These are the attributes of the class"""

    def __init__(self, size=0):
        """
        Instance of all attributes
        Attribute:
            size: size
        """

        self.size = size

    """this method return the area of square"""
    def area(self):
        return self.__size * self.__size

    """This is getter method"""
    @property
    def size(self):
        return self.__size

    """This is setter method for size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
