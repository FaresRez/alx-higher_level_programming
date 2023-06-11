#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for i in matrix:
            if i:
                for j in i[:-1]:
                    print("{:d}".format(j), end=" ")
                print("{}".format(i[-1]))
            else:
                print("".format())
