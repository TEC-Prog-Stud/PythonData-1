#!/usr/bin/env python3

import numpy as np
import math

def solve_quadratic(a, b, c):
    ansPos = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    ansNeg = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return (ansPos, ansNeg)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))

if __name__ == "__main__":
    main()
