#!/usr/bin/python3
""" Task 7 """
import os
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists ('add_item.json'):
    json_file = load_from_json_file('add_item.json')
else:
    json_file = []

for i in range(1, len(sys.argv)):
    json_file.append(sys.argv[i])

save_to_json_file(json_file, 'add_item.json')
