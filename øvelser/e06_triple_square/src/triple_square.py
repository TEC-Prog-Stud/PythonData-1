#!/usr/bin/env python3


def main():
    def triple(x):
        return x*3

    def square(y):
        return y*y

    for i in range(10):
        print(triple(i))
        print(square(i))
        if square(i) > triple(i):
            break

if __name__ == "__main__":
    main()
