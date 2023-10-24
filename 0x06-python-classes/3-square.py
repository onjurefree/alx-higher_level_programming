#!/usr/bin/python3
"""
This is class square
"""


class Square:

    """This are the attributes"""

    def __init__(self, size=0):

        """
        This are the attributes of this class

        Atrribute:
            size: size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    """This is class method"""
    def area(self):
        return self.__size * self.__size
