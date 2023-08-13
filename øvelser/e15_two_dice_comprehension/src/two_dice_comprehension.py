#!/usr/bin/env python3

def main():
    L = []
    for i in range(1, 7):
        L.clear()
        L.append(i)
        for x in range(1,7):
            if i + x == 5:
                L.append(x)
                print(L)

if __name__ == "__main__":
    main()
