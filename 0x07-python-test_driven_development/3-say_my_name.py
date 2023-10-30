#!/usr/bin/python3
"""
This function prints the first and last names
The function takes in two args
The args must be strings
"""


def say_my_name(first_name, last_name=""):
    """printing names"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
