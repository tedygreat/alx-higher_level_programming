#!/usr/bin/python3


"""
module for calculation of n-queens problem
"""
import sys


class Solution_Board:
    """class for use with n queens problem
    """
    solutions = []

    def __init__(self, num):
        self.num = num

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if not isinstance(num, int):
            raise TypeError("num should be an int")
        self.__num = value

args = sys.argv

if len(args) != 2:
    exit(1)
if not args[1].isdigit():
    print("N must be a number")
    exit(1)

num = int(args[1])
if num < 4:
    print("N must be at least 4")
    exit(1)
