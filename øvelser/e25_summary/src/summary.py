#!/usr/bin/env python3

import sys
import math

def summary(filename=r"øvelser\e25_summary\src\example.txt"):
    print(filename)
    L = []
    with open(filename) as f:
        for l in f:
            try:
                L.append(float(l))
            except ValueError:
                pass
    s = sum(L)
    a = s/len(L)
    k = 0
    for x in L:
        k += (x - a)**2
    std = math.sqrt(k/(len(L) -1 ))


    return (s,a,std)
    
def main():
    for filename in sys.argv[1:]:
        #print(summary(filename))
        s = summary(filename)
        print(f'File: {filename} Sum: {s[0]:.6f} Average: {s[1]:.6f} Stddev: {s[2]:.6f}')

if __name__ == "__main__":
    main()
