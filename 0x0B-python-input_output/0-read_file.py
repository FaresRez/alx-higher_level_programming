#!/usr/bin/python3
def read_file(filename=""):
    """
        read a given file
    """
    with open(filename, 'r') as f:
         f.read()
         f.close()
