#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                i += 1
        except TypeError:
            pass
        except IndexError:
            print("IndexError: List index out of range")
    print()
    return j
