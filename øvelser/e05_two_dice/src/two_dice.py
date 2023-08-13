#!/usr/bin/env python3
import random

def main():
    # d = list(range(1,5))
    # random.shuffle(d)
    # for i in d:
    #     x = i
    #     for i in d:
    #         if i + x == 5:
    #             print("(%x, %i)" % (x, i))

    for i in range(1, 7):
        for x in range(1,7):
            if i + x == 5:
                print("(%i, %x)" % (i, x))


if __name__ == "__main__":
    main()
