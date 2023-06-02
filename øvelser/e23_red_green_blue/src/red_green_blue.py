#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    L = []
    pat = r'(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.*)'
    with open(filename, 'r') as f:
        for line in f:
            mo = re.search(pat, line)
            if mo:
                res = '\t'.join(mo.groups())
                L.append(res)
    return L


def main():
    red_green_blue()
    pass

if __name__ == "__main__":
    main()
