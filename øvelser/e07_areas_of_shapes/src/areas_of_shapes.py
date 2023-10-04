#!/usr/bin/env python3

import math

def areaTriangle(h, b):
        return (float(h)*float(b))/2

def areaRectangle(h, b):
        return float(h)*float(b)

def areaCicle(r):
        return math.pi*(float(r)**2)

def isNumber(x):
    return (x is int or x is float) or (type(x) is str and x.replace(".", "").isnumeric())

def main():
    while(True):
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if (shape.lower() == "triangle"):
            b = input("Give base of the triangle: ")
            h = input("Give height of the triangle: ")
            if isNumber(h) and isNumber(b):
                print(f"The area is {round(areaTriangle(h, b),4)}")
        elif (shape.lower() == "rectangle"):
            b = input("Give width of the rectangle: ")
            h = input("Give height of the rectangle: ")
            if isNumber(h) and isNumber(b):
                print(f"The area is {round(areaRectangle(h, b),4)}")
        elif (shape.lower() == "circle"):
            r = input("Give radius of the circle: ")
            if  isNumber(r):
                print(f"The area is {round(areaCicle(r),4)}")
        elif (shape.lower() == ""):
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
