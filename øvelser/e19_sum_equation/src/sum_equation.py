#!/usr/bin/env python3

def sum_equation(nums):
    if len(nums) == 0:
        return '0 = 0'
    else:
        return ' + '.join(map(str, nums)) + ' = ' + str(sum(nums))

def main():
    pass

if __name__ == "__main__":
    main()
