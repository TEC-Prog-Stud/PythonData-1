#!/usr/bin/env python3
import math
import sys

def summary(filename):
    t = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                t.append(float(line))
            except ValueError:
                pass

    def SD(x):
        gns = sum(x)/len(x)
        s = sum( [(xi - gns)**2 for xi in x])

        return math.sqrt( s / (len(x) - 1))
    
    s = sum(t)
    a = sum(t)/len(t)
    sd = SD(t)
    return (s,a,sd)

def main():
    # To run write: python .\src\summary.py .\src\example.txt. In Python Terminal, in the right directory
    files = sys.argv[1:]
    for filename in files:
        s,a,sd = summary(filename)
        print(f'File: {filename} Sum: {s:.6f} Average: {a:.6f} Stddev: {sd:.6f}')

if __name__ == "__main__":
    main()
