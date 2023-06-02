#!/usr/bin/env python3

def main():
    for i in range(1, 7):
        for n in range(1,7):
                if i+n == 5:
                    print((i,n))
                else:
                    'print("(", i, ",", n, ") =", i+n)'
    pass

if __name__ == "__main__":
    main()
