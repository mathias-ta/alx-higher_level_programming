#!/usr/bin/python3
"""
A scriptto add all arguments to a Python list and
save them to a file
"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    existing_content = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], "add_item.json")
