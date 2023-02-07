#!/usr/bin/env python3

def transform(s1, s2):
    l1 = list(map(int, s1.split()))
    l2 = list(map(int, s2.split()))
    
    # z = list(zip(s1.split(), s2.split()))
    # L = list(map(lambda t : int(t[0]) * int(t[1]), z))
    
    return [x*y for x, y in zip(l1, l2)]

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
