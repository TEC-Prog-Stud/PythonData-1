#!/usr/bin/env python3

def merge(L1, L2):
    result = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    result += L1[i:]
    result += L2[j:]
    return result


def main():
    L1 = [10, 30, 50, 70]
    L2 = [20, 40, 60, 80, 100]
    L = merge(L1, L2)
    print(L)  # [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == '__main__':
    main()
