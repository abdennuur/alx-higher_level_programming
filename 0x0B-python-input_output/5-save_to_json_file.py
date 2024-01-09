#!/usr/bin/python3
"""
function that write object to text file
"""

import json


def save_to_json_file(my_obj, filename):
    """Object to text file, using JSON representation"""
    with open(filename, 'w', encoding='utf-8') as fl:
        json.dump(my_obj, fl)
