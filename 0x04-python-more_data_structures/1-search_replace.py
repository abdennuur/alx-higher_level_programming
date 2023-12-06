#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    return [v if v != search else replace for v in my_list]
