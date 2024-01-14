#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    idx = 0

    try:
        for i in my_list:
            if idx < x:
                print('{}'.format(my_list[idx]), end='')
                idx += 1

        print()
    except TypeError:
        pass
    finally:
        return idx


# safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))