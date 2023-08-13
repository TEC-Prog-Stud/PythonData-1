#!/usr/bin/env python3

def interleave(*lists):
    newlist = []
    for i in list(zip(*lists)):
        newlist.append(list(i))
    
    return newlist

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
