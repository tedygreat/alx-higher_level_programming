#!/usr/bin/python3
def no_c(my_string):
    listofchars = list(my_string)
    new = ""
    for char in my_string:
        if (char != 'c' or char != 'C'):
            new += char
    return(new)
