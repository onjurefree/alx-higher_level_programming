#!/usr/bin/python3
"""
This is class rectangle with four method and magit methods str and repr
"""


class Rectangle:
    """these are the attributes"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """This str method return shape in #"""
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        shape = ""
        for _ in range(self.__height):
            shape += "#" * self.__width + "\n"
        return shape

    """This repr method return string representation of rectangle"""
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    """this method gets called every time instance is deleted"""
    def __del__(self):
        print("Bye rectangle...")

    """This method sets width"""
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

    """this method returns area"""
    def area(self):
        return self.__width * self.__height

    """This method returns perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
