#!/usr/bin/python3
"""
contains method to save object to JSON file
"""


def save_to_json_file(my_obj, filename):
    """Save my_obj to JSON"""
    import json
    with open(filename, mode="w", encoding="utf-8") as f_name:
        json.dump(my_obj, f_name)
