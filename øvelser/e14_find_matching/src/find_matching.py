#!/usr/bin/env python3

def find_matching(L, pattern):
    res = []
    for tup in enumerate(L, 0):
        if pattern in tup[1]:
            res.append(tup[0])
    return res

def find_matching2(L, pattern):
    res = []
    for string in L:
        if pattern in string:
            res.append(L.index(string))
    return res

def main():
   print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
