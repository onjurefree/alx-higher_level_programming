#!/usr/bin/python3
"""
A Function that adds intergers
The numbers must be ints or floats
The result is always int
"""


def add_integer(a, b=98):
    """
    this function adds var a and var b
    var a or be must be floats or ints
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
