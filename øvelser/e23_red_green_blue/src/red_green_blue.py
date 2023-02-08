#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    L = []
    lines = []
    with open(filename, 'r') as f:
        for l in f:
            rx = r'^\s*(\d+)\s*(\d+)\s*(\d+)\s*(.*?)\n$'
            r = re.search(rx, l)
            if r:
                g = r.groups()
                m = (g[0] + '\t')
                m = '\t'.join(g)
                L.append(m)
    return L


def main():
    pass


if __name__ == "__main__":
    main()
