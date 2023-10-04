#!/usr/bin/env python3

def transform(s1, s2):
    res = []
    if s1 and s2:
        # numbers1 = list(map(int, s1.split(" ")))
        # numbers2 = list(map(int, s2.split(" ")))
        # zipped = zip(numbers1, numbers2)
        # zipped = zip(map(int, s1.split(" ")), map(int, s2.split(" ")))
        res = [x[0]*x[1] for x in zip(map(int, s1.split(" ")), map(int, s2.split(" ")))]
    return res

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
