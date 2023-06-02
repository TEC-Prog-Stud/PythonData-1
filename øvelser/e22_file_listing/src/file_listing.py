#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    L = []
    pat = r'(\d+) (\w{3})\s+(\d{1,2}) (\d\d):(\d{2}) (.*)$'
    with open(filename, 'r') as f:
        for line in f:
            mo = re.search(pat, line)
            if mo:
                data = mo.groups()
                
                res = (int(data[0]), data[1], int(data[2]), int(data[3]), int(data[4]), data[5])
                L.append(res)
    return L

def main():

    pass

if __name__ == "__main__":
    main()
