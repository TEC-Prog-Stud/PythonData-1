#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        linecount = len(lines)
        wordcount = 0
        charcount = 0
        for line in lines:
            words = line.split()
            wordcount += len(words)
            charcount += len(line)
        return (linecount, wordcount, charcount)

def main():
    for filename in sys.argv[1:]:
        linecount, wordcount, charcount = file_count(filename)
        
        print(linecount,'\t',wordcount,'\t', charcount,'\t',filename)

if __name__ == "__main__":
    main()
