#!/usr/bin/python3
"""module contain a function that multiplies two matrix"""


def matrix_mul(m_a, m_b):
    """matrix_mul function multiplie two matrix
    Args:
        m_a (list of lists): the first matrix
        m_b (list of lists): the second matrix
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    # variables verify if both m_a and m_b can be multiplied
    num_colum1 = 0
    num_row2 = 0

    # Check requirements for the matrix m_a
    if m_a == []:
        raise ValueError("m_a can't be empty")
    for rw1 in m_a:
        if type(rw1) != list:
            raise TypeError("m_a must be a list of lists")
        ln1 = len(m_a[0])
        if rw1 == []:
            raise ValueError("m_a can't be empty")
        if ln1 != len(rw1):
            raise TypeError("each row of m_a must be of the same size")
        num_colum1 = len(rw1)
        for column1 in rw1:
            if type(column1) != int and type(column1) != float:
                raise TypeError("m_a should contain only integers or floats")

    # Check requirements for matrix m_b
    if m_b == []:
        raise ValueError("m_b can't be empty")
    for rw2 in m_b:
        if type(rw2) != list:
            raise TypeError("m_b must be a list of lists")
        ln2 = len(m_b[0])
        if rw2 == []:
            raise ValueError("m_b can't be empty")
        if ln2 != len(rw2):
            raise TypeError("each row of m_b must be of the same size")
        num_row2 += 1
        for column2 in rw2:
            if type(column2) != int and type(column2) != float:
                raise TypeError("m_b should contain only integers or floats")

    # Check if the multiplication is posible
    if num_colum1 != num_row2:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    for rw_1 in m_a:
        i = 0
        l_row = []
        while i < len(m_b[0]):
            result = 0
            ka = 0
            for column_1 in rw_1:
                result += column_1 * m_b[ka][i]
                ka += 1
            l_row.append(result)
            i += 1
        mul_matrix.append(l_row)

    return mul_matrix
