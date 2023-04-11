#!/usr/bin/python3


""" 0x0B-python-input_output task 2 """


def append_write(filename="", text=""):
    """appends onto a utf-8 encoded text file
    """
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
