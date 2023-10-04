#!/usr/bin/env python3

def triple(x):
    return x*3

def square(x):
    return x**2
    
# end def

def main():
    for x in range(1, 11):
        tx = triple(x)
        sx = square(x)
        if sx > tx:
            break
        print(f"triple({x})=={tx} square({x})=={sx}")
    
if __name__ == "__main__":
    main()
