#!/usr/bin/python3


"""0x0A-python-inheritance task 1 """


class MyList(list):
    """ extended version of list
    """
    def print_sorted(self):
        """prints the list in ascending order
        """
        copy = self[:]
        copy.sort()
        print(copy)
