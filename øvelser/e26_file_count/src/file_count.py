#!/usr/bin/env python3

import sys

def file_count(filename):
    f = open(filename, "r")
    lines = f.readlines()
    words = []
    chars = []
    for line in lines:
        ws = line.split()
        for word in ws:
            words.append(word)
        for char in line:
            chars.append(char)
    
    return (len(lines), len(words), len(chars))

def main():
    for arg in sys.argv[1:]:
        ans = file_count(arg)
        print(f"{ans[0]}\t{ans[1]}\t{ans[2]}\t{arg}")

if __name__ == "__main__":
    main()
