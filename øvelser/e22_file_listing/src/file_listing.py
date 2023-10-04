#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    res = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        
    return res

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
