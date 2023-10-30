#!/usr/bin/python3
"""
This function multiply matrices
The elements of the matrices must be list of int or floats
"""


def matrix_mul(m_a, m_b):
    """This function multipy matrix"""

    status = check_if_list(m_a)
    if status == "False":
        raise TypeError("m_a must be a list")
    elif check_if_list(m_a) == "empty":
        raise ValueError("m_a can't be empty")

    status = check_if_list(m_b)
    if status == "False":
        raise TypeError("m_b must be a list")
    elif status == "empty":
        raise ValueError("m_b can't be empty")

    status_list = check_if_list_of_list(m_a)
    if status_list == "False":
        raise TypeError("m_a must be a list of lists")
    elif status_list == "empty":
        raise ValueError("m_a can't be empty")

    status_list = check_if_list_of_list(m_b)
    if status_list == "False":
        raise TypeError("m_b must be a list of lists")
    elif status_list == "empty":
        raise ValueError("m_b can't be empty")

    if not int_or_float(m_a):
        raise TypeError("m_a should contain only integers or floats")

    if not int_or_float(m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not equal_rows(m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not equal_rows(m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    #  multipying the matrices now
    result = [[0] * len(m_b[0]) for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result


def check_if_list(m_a):
    """We are checking if its list"""

    if len(m_a) == 0:
        return "empty"

    if not isinstance(m_a, list):
        return "False"
    return "True"


def check_if_list_of_list(m_a):
    """We are checking if its list of lists"""

    for element in m_a:

        if not isinstance(element, list):
            return "False"

        if len(element) == 0:
            return "empty"
    return "True"


def int_or_float(m_a):
    """We are checking if values are floats"""

    for elements in m_a:
        for element in elements:
            if not isinstance(element, (int, float)):
                return False

    return True


def equal_rows(m_a):
    """we are checking if rows are equal"""

    size = len(m_a[0])
    for elements in m_a[1:]:
        if len(elements) != size:
            return False

    return True
