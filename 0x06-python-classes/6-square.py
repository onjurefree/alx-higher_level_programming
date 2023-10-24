#!/usr/bin/python3
"""
This is class square with its attributes
"""


class Square:

    """This are the attributes"""

    def __init__(self, size=0, position=(0, 0)):

        """
        Attributes of the class

        Atrribyutes:
            size: size
            position: position
        """

        self.size = size
        self.position = position

    """This method finds area of the square"""
    def area(self):
        return self.__size * self.__size

    """This method gets the size of square"""
    @property
    def size(self):
        return self.__size

    """This method sets the size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """This method prints # for both sides of the square"""
    def my_print(self):
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()

        for j in range(self.__size):
            for h in range(self.__position[0]):
                print(" ", end="")

            for k in range(self.__size):
                print("#", end="")
            print()

    """This method returns position"""
    @property
    def position(self):
        return self.__position

    """This method sets the position"""
    @position.setter
    def position(self, value):
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
