#!/usr/bin/env python3

def merge(L1, L2):
    merged = []
    x = 0
    y = 0
    
    while x < len(L1) and y < len(L2):
        if L1[x] <= L2[y]:
            merged.append(L1[x])
            x += 1
        else:
            merged.append(L2[y])
            y += 1
    
    while x < len(L1):
        merged.append(L1[x])
        x += 1
    
    while y < len(L2):
        merged.append(L2[y])
        y += 1
    
    return merged


def main():
    pass

if __name__ == "__main__":
    main()
