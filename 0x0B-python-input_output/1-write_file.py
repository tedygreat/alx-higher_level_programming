#!/usr/bin/python3


""" 0x0B-python-input_output task 0"""


def read_file(filename=""):
    """reads a file
    """
    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end='')
