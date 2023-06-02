#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        print(end="\n")
        for n in range(1, 11):
            print(f"{n*i: 4d}", end="")
    pass

if __name__ == "__main__":
    main()
