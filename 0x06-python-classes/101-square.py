#!/usr/bin/python3
"""
This is class Square with its attributes
"""


class Square:
    """These are the attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """The attributes
        Attribute:
            size: size
            position: position
        """
        self.size = size
        self.position = position

    """This method returns size"""
    @property
    def size(self):
        return self.__size

    """This method sets size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """This method returns position"""
    @property
    def position(self):
        return self.__position

    """This method sets position"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """This method returns are"""
    def area(self):
        return self.__size * self.__size

    """This method prints squire"""
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    """This method define square representation"""
    def __str__(self):
        squ = ""
        if self.__size == 0:
            return squ

        squ += "\n" * self.__position[1]
        for _ in range(self.__size):
            squ += " " * self.__position[0] + "#" * self.__size + "\n"
        return squ[:-1]
