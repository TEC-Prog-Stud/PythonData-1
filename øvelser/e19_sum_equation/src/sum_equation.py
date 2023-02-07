#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        s = "0 = 0"
    else:
        s = " + ".join(map(str,L))
        s += " = " + str(sum(L))
    return s

def main():
    print(sum_equation([1,5,7]))


if __name__ == "__main__":
    main()
