#!/usr/bin/env python3

import re

def mapFunc(n: str):
    if n.isnumeric():
        return int(n)
    else: return n

def file_listing(filename="src/listing.txt"):
    res = []
    f = open(filename, "r")
    pattern = r'(\d+)\s(\w{3})\s+(\d+)\s(\d+):(\d+)\s(.*?)$'
    for line in f:
      match = re.search(pattern, line)
      groups = match.groups()
      res.append(tuple(map(mapFunc, groups)))
    f.close()

    return res

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
