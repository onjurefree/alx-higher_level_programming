#!/usr/bin/python3
"""
This is class rectangle and its methods
"""


class Rectangle:
    """these are the attributes of this class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """This method returns str in shape #"""
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        shape = ""
        for _ in range(self.__height):
            shape += "#" * self.__width + "\n"
        return shape[:-1]

    """This method return string representation of rectangle"""
    def __repr_(self):
        return f"Rectangle({self.__width}, {self.__height})"

    """This method gets called everytime an instance is deleted"""
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
            raise TypeError("height must be >= 0")

        self.__height = value

    """This method returns area"""
    def area(self):
        return self.__width * self.__height

    """this method return perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width * self.__height)

    """This method compares rectangle sizes"""
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
