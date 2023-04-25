#!/usr/bin/env python3

def triple(x):
    return x*3


def square(y):
    return y**2

def main():

    for i in range(1, 11):
        # print('triple(', i, ') ==', triple(i), sep='')
        t = triple(i)
        s = square(i)

        if t < s:
            break
        print(f"triple({i})=={t} square({i})=={s}")


if __name__ == "__main__":
    main()
