#!/usr/bin/python3
"""This is class MagicClass with its attributes"""


import math


class MagicClass:
    """This are the attributes"""

    def __init__(self, radius=0):
        """
        This are the attributes of this class
        Attributes:
            radius: radius
        """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """This method returns area"""
    def area(self):
        return (self.__radius ** 2 * math.pi)

    """This method return circumference"""
    def circumference(self):
        return (2 * math.pi * self.__radius)
