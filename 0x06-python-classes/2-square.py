#!/usr/bin/python3
"""
This is a class model
"""


class Square:

    """Class square with attributes"""

    def __init__(self, size=0) -> None:
        """
        Class atributes are here

        Attributes:
            size: size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
