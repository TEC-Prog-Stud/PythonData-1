#!/usr/bin/env python3

import math


def main():
    def triangle():
        b = float(input("Give base of the triangle: "))
        h = float(input("Give height of the triangle: "))
        a = (1/2)*h*b
        print("The area is %a" % (a))
    
    def rectangle():
        w = float(input("Give width of the rectangle: "))
        h = float(input("Give height of the rectangle: "))
        a = w * h
        print("The area is %a" % (a))
    
    def circle():
        r = float(input("Give radius of the circle: "))
        a = 3.14159265 * r**2
        print("The area is %a" % (a))
    
    while True == 1:
        s = input("Choose a shape (triangle, rectangle, circle): ")
        if s == "triangle":
            triangle()
        elif s == "rectangle":
            rectangle()
        elif s == "circle":
            circle()
        elif s == "":
            break
        else:
            print("Unknown shape!")
            
            
        
    
    

if __name__ == "__main__":
    main()
