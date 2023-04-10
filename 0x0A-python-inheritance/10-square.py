#!/usr/bin/python3


"""0x0A-python-inheritance task 10 """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square shape class, super class is BaseGeometry, then Rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
