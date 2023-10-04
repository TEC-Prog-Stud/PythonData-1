#!/usr/bin/env python3

def detect_ranges(P):
    L = sorted(P)
    newList = []
    upper = 0
    lower = 0
    x = 0
    
    while x < len(L):
        lower = L[x]
        upper = lower
        count = 1
        
        while(x+count < len(L) and  upper +1 == L[x+count]):
            upper += 1
            x += 1    
            count = +1
            if x+count > len(L):
                break
        
        if (lower < upper):
            newList.append((lower,upper+1))
        else:
            newList.append(lower)
        x += 1
        if x > len(L):
            break
        
    return newList
    

def main():
    L = [0, 37, 38, 7, 74, 12, 80, 55, -38, -65]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
