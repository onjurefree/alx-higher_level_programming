#!/usr/bin/python3
"""
This model is for division of matrix
All values must be ints or floats
return new matrix
"""


def matrix_divided(matrix, div):
    """
    div must not be 0
    all members of the matrix should be ints or floats
    returns a new list
    """
    for element in matrix:
        for var in element:
            if not isinstance(var, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    """function that checks type of val"""
    if not matrix_len(matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    for row in matrix:
        row_list = []
        for var in row:
            result = round(var / div, 2)
            row_list.append(result)

        new_list.append(row_list)

    return new_list


"""
funtion that takes in matrix
it chacks if all rows of matrix have some length
check of the matrix is empty
"""


def matrix_len(matrix):
    if len(matrix) == 0:
        return False

    row_size = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != row_size:
            return False
    return True
