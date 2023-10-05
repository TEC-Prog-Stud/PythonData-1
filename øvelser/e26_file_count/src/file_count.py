#!/usr/bin/env python3

import sys

def file_count(filename):
    f = open(filename, "r")
    lines = f.readlines()
    words = []
    chars = 0
    for line in lines:
        chars += len(line)
        ws = line.split()
        for word in ws:
            words.append(word)
    f.close()
    
    return (len(lines), len(words), chars)

def main():
    for arg in sys.argv[1:]:
        ans = file_count(arg)
        print(f"{ans[0]}\t{ans[1]}\t{ans[2]}\t{arg}")
    
    # ans = file_count("src/test.txt")
    # print(f"{ans[0]}\t{ans[1]}\t{ans[2]}\tsrc/test.txt")

if __name__ == "__main__":
    main()
