#!/usr/bin/python3
"""This is class square"""


class Square:
    """Attributes of this class"""

    def __init__(self, size=0):
        """Atributes of the class
        Atrribute
        size: size
        """
        self.size = size

    """This method returns the size"""
    @property
    def size(self):
        return self.__size

    """This method sets the size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """This method returns the area"""
    def area(self):
        return self.__size * self.__size

    """This methods compare self and others"""
    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
