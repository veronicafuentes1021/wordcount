#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "Veronica Fuentes and Daniel Lomelino"

import sys


def create_word_dict(filename):
    my_dict = {}
    with open(filename) as text:
        for line in text:
            line = line.lower()
            words = line.split()
            for word in words:
                if word in my_dict:
                    my_dict[word] = my_dict[word] + 1
                else:
                    my_dict[word] = 1
    sorted_dict = {}
    for word, count in sorted(my_dict.items()):
        sorted_dict[word] = count
    return sorted_dict


def print_words(filename):
    my_dict = create_word_dict(filename)
    for key in list(my_dict.keys()):
        print(key, ":", my_dict[key])


def print_top(filename):
    the_dict = create_word_dict(filename)
    sort_count = sorted(the_dict.items(), key=lambda v: v[1], reverse=True)
    for i in range(20):
        if i >= len(sort_count):
            break
        word, count = sort_count[i]
        print(word, ":", count)


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
