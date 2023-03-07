#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    coun = len(str)
    for i in range(coun):
        char = ord(str[i])
        if i == n:
            continue
        else:
            newstr += format(chr(char))
    return newstr
