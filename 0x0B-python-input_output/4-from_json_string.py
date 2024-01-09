#!/usr/bin/python3
"""
contain json stri function
"""

import json


def from_json_string(my_str):
    """return object represented by JSON str"""
    return json.loads(my_str)
