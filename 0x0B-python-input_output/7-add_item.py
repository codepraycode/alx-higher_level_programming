#!/usr/bin/python3
"""A script that adds all arguments to a Python list,
    and then save them to a file
"""
import sys
from os import path


# Load functions from other modules
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

# CONSTANTS: File name for export
FILE_NAME = "add_item.json"

# Length of terminal argument
_arg_count = len(sys.argv)

# list: List of files
file_lists = []

if path.exists(FILE_NAME):
    file_lists = load_from_json_file(FILE_NAME)

if _arg_count == 1:
    save_to_json_file(file_lists, FILE_NAME)
else:
    for each_i in range(1, _arg_count):
        file_lists.append(sys.argv[each_i])

    save_to_json_file(file_lists, FILE_NAME)
