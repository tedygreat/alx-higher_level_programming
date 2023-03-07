#!/usr/bin/python3
def remove_char_at(str, n):
    coun = len(str)
    for i in range(coun):
        char = ord(str[i])
        if i == n:
            continue
        else:
            print("{}".format(chr(char)), end="")
