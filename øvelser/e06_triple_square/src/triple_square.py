#!/usr/bin/env python3


def triple(t):
    "This is multi with 3"
    t = t* 3
    return(t)


def square(s):
    "This use power of 2"
    s = s **2
    return(s)

def main():
    for i in range(1,11):
        ts = triple(i)    
        st = square(i)
        if ts < st:
            break
        else:
            print(f"triple({i})=={ts}", f"square({i})=={st}")

if __name__ == "__main__":
    main()
