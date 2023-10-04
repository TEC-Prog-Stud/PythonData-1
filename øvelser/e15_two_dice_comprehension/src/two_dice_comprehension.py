#!/usr/bin/env python3

def main():
    diceComp = [(x,y) for x in range(1, 7) for y in range(1,7) if x+y == 5]
    print(*diceComp, sep="\n")
    
if __name__ == "__main__":
    main()
