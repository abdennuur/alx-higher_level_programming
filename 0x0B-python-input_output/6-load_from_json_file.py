#!/usr/bin/python3
"""
function that create an Object from JSON file
"""

import json


def load_from_json_file(filename):
    """create object frm JSON file """
    with open(filename, 'r', encoding='utf-8') as fl:
        return json.load(fl)
