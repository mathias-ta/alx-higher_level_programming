#!/usr/bin/python3
"""
contains method to change from JSON format
"""


def from_json_string(my_str):
    """Change my_str from JSON"""
    import json
    return json.loads(my_str)
