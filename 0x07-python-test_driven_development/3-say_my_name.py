#!/usr/bin/python3
"""
Say My Name - a function that says your name.
"""
def say_my_name(first_name, last_name=""):
    """
    Says your name.
    first_name and last_name must be strings otherwise, will raise a TypeError
    """
    # first_name must be an integer
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    # last_name must be string
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

# 3-say_my_name.py
"""Defines a name-printing function."""
def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
