#!/usr/bin/env python3

def interleave(*lists):
    res = []
    zipList = list(zip(*lists))
    for x in zipList:
        res.extend(x)
    
    return res

def interleave2(*lists):
    res = []
    for x in range(len(lists[0])):
        for y in range(len(lists)):
            res.append(lists[y][x])
            
    return res


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))
    print(interleave([41, -61, 51, -60, 0, -78, 88, 36, -91, 95], [4, 5, 82, 18, -41, -30, -38, 65, -95, -2], [69, -18, -40, 97, 24, -42, -51, 3, 12, 93], [61, 42, 21, 52, -41, 91, -84, 88, 15, -23]))
    print(interleave2([41, -61, 51, -60, 0, -78, 88, 36, -91, 95], [4, 5, 82, 18, -41, -30, -38, 65, -95, -2], [69, -18, -40, 97, 24, -42, -51, 3, 12, 93], [61, 42, 21, 52, -41, 91, -84, 88, 15, -23]))

if __name__ == "__main__":
    main()
