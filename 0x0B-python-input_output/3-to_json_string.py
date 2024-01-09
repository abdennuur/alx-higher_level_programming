#!/usr/bin/python3
"""
contain JSON str
"""

import json


def to_json_string(my_obj):
    """return JSON representation of object (str)"""
    return json.dumps(my_obj)
