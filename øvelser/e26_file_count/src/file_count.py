#!/usr/bin/env python3

import sys

def file_count(filename="src/test.txt"):
    with open(filename, "r") as f:
        txt = f.read()
    
    lines = txt.count('\n') #len(txt.split("\n"))
    words = len(txt.split())
    chars = len(txt)


    return (lines, words, chars)

def main():
    #print(file_count(r'øvelser\e26_file_count\src\test.txt'))

    for f in sys.argv[1:]:
        r = file_count(f)
        print(*r, f, sep='\t')


if __name__ == "__main__":
    main()
