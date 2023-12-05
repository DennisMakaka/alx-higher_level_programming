#!/usr/bin/python3

if __name__ == "__main__":
    /* Importing the add function from add_0 module */
    from add_0 import add


    /* Defining variables a and b */
    a = 1
    b = 2

    /* Printing the sum of a and b using the add function */
    print("{} + {} = {}".format(a, b, add(a, b)))
