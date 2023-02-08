#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(
                r'(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+(.+)', line)
            if match:
                size, month, day, hour, minute, filename = match.groups()
                result.append((int(size), month, int(day),
                              int(hour), int(minute), filename))
    return result
def main():
    pass

if __name__ == "__main__":
    main()
