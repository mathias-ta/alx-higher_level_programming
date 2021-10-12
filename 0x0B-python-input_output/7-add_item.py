#!/usr/bin/python3
"""
A scriptto add all arguments to a Python list and
save them to a file
"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_name = "add_item.json"
try:
    existing_content = load_from_json_file(file_name)
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], file_name)
