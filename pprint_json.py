#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json


def get_args():
    """
    Supports the command-line arguments listed below.
    """
    parser = argparse.ArgumentParser(description='Pretty print any raw JSON file')
    parser.add_argument('file', metavar='JSON file', help='Path to incoming raw JSON file')
    args = parser.parse_args()
    return args


def load_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as open_file:
            return json.load(open_file)
    except FileNotFoundError:
        pass


def pretty_print_json(json_file):
    print(json.dumps(json_file, sort_keys=True, indent=4, ensure_ascii=False))


def _main():
    args = get_args()
    json_file = load_file(args.file)
    if json_file:
        pretty_print_json(json_file)
    else:
        print('File not found')


if __name__ == '__main__':
    _main()
