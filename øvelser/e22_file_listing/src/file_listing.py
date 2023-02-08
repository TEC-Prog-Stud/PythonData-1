#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    with open(filename, "r") as f:
        for line in f:
            regex = r"\s+(\d+)\s([A-Za-z]{3})\s+(\d+)\s(\d)+:(\d+)\s([-_.A-Za-z \d]+)"
            res = re.search(regex, line)
            if res:
                print(res.groups())    
                g = res.groups()
                t = (
                    int(g[0]),
                    g[1],
                    int(g[2]),
                    int(g[3]),
                    int(g[4]),
                    g[5]
                )
                print(t)
                result.append(t)
    return result

def main():
    print(file_listing(r'øvelser\e22_file_listing\src\listing.txt'))


if __name__ == "__main__":
    main()
