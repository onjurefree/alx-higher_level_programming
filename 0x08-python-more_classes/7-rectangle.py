#!/usr/bin/python3
"""
This is class rectangle
"""


class Rectangle:
    """This is this classe attributes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """This method return shape in #"""
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = ""
        for _ in range(self.__height):
            shape += str(self.print_symbol) * self.__width + "\n"
        return shape[:-1]

    """This method returns string representation of rectangle"""
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    """This method gets call when instances are deleted"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """This method returns width"""
    @property
    def width(self):
        return self.__width

    """This method sets width"""
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

    """this method sets height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """This method reurns area"""
    def area(self):
        return self.__width * self.__height

    """This method returns perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width * self.__height)
