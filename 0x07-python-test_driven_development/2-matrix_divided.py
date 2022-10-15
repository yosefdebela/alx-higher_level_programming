#!/usr/bin/python3
"""
This is the divide module.
has a function to divide matrix
Divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """matrix must be a list of lists of integers/floats
    Returns a new matrix
    """
    newmatrix = []
    length = 0

    # Divides all elements of a matrix
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError('div must be a number')
    # Matrix must be a list of integers or floats, TypeError
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    # mats aof the specified number
            # with the specified number of decimals
            newrow.append(round(item / div, 2))
     to 0
    if len(matrix[0]) <= 0:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    # 1.let's create new matrix with newrow
    for row in matrix:
        newrow = []
        # matrix raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        # 2. row is empty
        if length is 0:
            length = len(row)
        # Each row must be the same size, TypeError
        elif leow of the matrix must have the same size')
        # 3. each item has to be an integer or float
        for item in rnot float:
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')
            # 4. add content to the row
            # elements will be divided by div 
