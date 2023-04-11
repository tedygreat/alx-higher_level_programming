#!/usr/bin/python3


""" class """


def class_to_json(obj):
    """creates a json representation of an object without using
        json module. One liner!! (without pep8 fix) :D
    """
    return vars(obj)
