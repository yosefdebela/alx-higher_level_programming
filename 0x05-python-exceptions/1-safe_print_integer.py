#!/usr/bin/python3
# 1-safe_print_integer.py
def safe_print_integer(value):
    try:
        print('{:d}'.format(value))
        return True
      except (TypeError, ValueError):
        print("non integer value is given")
        return False
value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))