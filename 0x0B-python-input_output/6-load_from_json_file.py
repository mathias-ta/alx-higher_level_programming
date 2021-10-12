#!/usr/bin/python3
"""
contains method to load object from JSON file
"""


def load_from_json_file(filename):
    """Load object from JSON"""
    import json
    with open(filename, mode="r", encoding="utf-8") as f_name:
        return json.load(f_name)
