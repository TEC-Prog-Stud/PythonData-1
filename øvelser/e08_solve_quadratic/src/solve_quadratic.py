#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    d= math.sqrt(b*b -4*a*c)
    positive = (-b + d) / (2*a)
    negative = (-b -d) / (2*a)

    return (positive,negative)


def main():
    pass

if __name__ == "__main__":
    main()
