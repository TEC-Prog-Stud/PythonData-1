#!/usr/bin/env python3

def sum_equation(L):
    if L:
        result = ""
        total = 0
        for index in range(len(L)):
            total += L[index]
            if index + 1 == len(L):
                result += f"{L[index]} = {total}"
            else:
                result += f"{L[index]} + "
    else:
        result = "0 = 0"
    return result

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
