#!/usr/bin/python3
<<<<<<< HEAD
"""
Print Square module, for printing squares with "#".

useful for all square-based applications
"""


def print_square(size):
    """size is the size length of the square
    size must be an integer
    """

    # size must be an integer, otherwise raise a TypeError
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    # if size is less than 0, raise a ValueError
    if size < 0:
        raise ValueError('size must be >= 0')
    # size is equal to lado por lado

    for x in range(size):
        print('#' * size)

=======
# 4-print_square.py
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
>>>>>>> d18cc8ec958c9b025557a4d503ca7454310e2fdb
