#!/usr/bin/env python3

import statistics
import sys


def summary(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                x = float(line.strip())
                numbers.append(x)
            except ValueError:
                # ignore lines that can't be converted to float
                pass
    if not numbers:
        return
    avg = statistics.mean(numbers)
    stddev = statistics.pstdev(numbers, avg)
    return sum(numbers), avg, stddev


def main():
    for filename in sys.argv[1:]:
        res = summary(filename)
        if res:
            sum_, avg, stddev = res
            print(
                f'File: {filename} Sum: {sum_:.6f} Average: {avg:.6f} Stddev: {stddev:.6f}')

if __name__ == "__main__":
    main()
