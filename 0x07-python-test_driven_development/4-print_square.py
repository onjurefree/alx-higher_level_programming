#!/usr/bin/python3
"""
This is a function that print square in #
Size must be a integer
size must be grater than 0
"""


def print_square(size):
    """This function prints square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size, end="")
        print()
