#!/usr/bin/python3
def safe_print_division(a, b):
    n = 0
    try:
        n = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {:.1f}".format(n))
    return n
