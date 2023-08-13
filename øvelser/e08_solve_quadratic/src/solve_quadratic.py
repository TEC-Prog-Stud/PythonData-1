#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        print("No solution")
    elif d == 0:
        x1 = -b/2*a
        x2 = -b/2*a
        result = (x1, x2)
        return result
    else:
        x1 = (-b + d**(1/2))/2*a
        x2 = (-b - d**(1/2))/2*a
        result = (x1, x2)
        return result



def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))
    

if __name__ == "__main__":
    main()
