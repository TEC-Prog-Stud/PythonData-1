#!/usr/bin/env python3

def merge(L1, L2):
    size1 = len(L1)
    size2 = len(L2)

    L = []

    i, j = 0, 0

    while i < size1 and j < size2:
        if L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
    L = L + L1[i:] + L2[j:]

    return L


def main():
   print(merge)


if __name__ == "__main__":
    main()
