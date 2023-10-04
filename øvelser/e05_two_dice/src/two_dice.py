#!/usr/bin/env python3

def main():
    for x in range(1,7):
        for y in range(1,7):
            if y+x == 5:
                print ("(" + str(x) + "," + str(y)+")")

if __name__ == "__main__":
    main()
