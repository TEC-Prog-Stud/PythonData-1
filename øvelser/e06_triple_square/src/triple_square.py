#!/usr/bin/env python3
def triple(x):
        'This function triples things'
        return x*3
def square(x):
        'This function squares things'
        return x*x

def main():
    
    
    for i in range(1,11):
        x= triple(i)
        y= square(i)
        if x < y:
            break
        print(f"triple({i})=={x} square({i})=={y}")
    pass

if __name__ == "__main__":
    main()
