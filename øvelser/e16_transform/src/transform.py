#!/usr/bin/env python3

def transform(s1, s2):
    z = list(zip(s1.split(), s2.split()))
    L = list(map(lambda t : int(t[0]) * int(t[1]), z))
    return L

def main():
    print(transform)

if __name__ == "__main__":
    main()
