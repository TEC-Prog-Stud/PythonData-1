#!/usr/bin/env python3


def main():
    for x in range(1, 11):
        for y in range(1, 11):
            ans = x*y
            print(str(ans)+"\t", end="")
        print("")

if __name__ == "__main__":
    main()
