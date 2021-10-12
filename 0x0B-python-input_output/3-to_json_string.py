#!/usr/bin/python3
"""
contains method to change to JSON format
"""


def to_json_string(my_obj):
    """Change my_obj to JSON"""
    import json
    return json.dumps(my_obj)
