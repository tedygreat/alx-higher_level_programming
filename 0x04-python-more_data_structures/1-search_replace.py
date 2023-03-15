#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            return (new_list[i] = replace)
        else:
            return (new_list[i] = my_list[i])
