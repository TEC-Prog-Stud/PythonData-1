#!/usr/bin/env python3

def merge(L1, L2):
    L = len(L1) + len(L2)
    return L

def main():
    L1 = sorted([5,3,7,1])
    L2 = sorted([6,4,2])
    merge(L1, L2)

if __name__ == "__main__":
    main()
