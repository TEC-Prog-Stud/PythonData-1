#!/usr/bin/env python3

import re

def file_extensions(filename):
    f = open(filename, "r")
    lines = f.readlines()
    pattern = r'\.[^.\s]*$'
    matches = [list(re.findall(pattern, line)).pop() for line in lines]
    for line in lines:
        matches += re.findall(pattern, line)
    return (matches, {})

def main():
    print(file_extensions("src/filenames.txt"))

if __name__ == "__main__":
    main()
