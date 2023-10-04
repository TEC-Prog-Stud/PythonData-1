#!/usr/bin/env python3

import sys
import math

def mapFloat(n):
    try:
        ans = float(n)
        return ans
    except Exception as e:
        return None

def mapFilter(n):
    if n == None:
        return False
    return True

def summary(filename):
    f = open(filename, "r")
    lines = list(filter(mapFilter,(map(mapFloat,f.readlines()))))
    print(lines)
    avg = sum(lines)/len(lines)
    std = 0
    for line in lines:
        std += (line-avg)**2
    std = math.sqrt(std/(len(lines)-1))
    f.close()
    
    return (sum(lines),avg,std)

def main():
    for arg in sys.argv[1:]:
        ans = summary(arg)
        print(f"File: {arg} Sum: {ans[0]:.6f} Average: {ans[1]:.6f} Stddev: {ans[2]:.6f}")

if __name__ == "__main__":
    main()
