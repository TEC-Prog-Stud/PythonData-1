#!/usr/bin/env python3

import math


def main():
    i = True
    while i == True:
        shape = input("Enter a shape (triangle, rectangle, circle): ")
        if (shape == "triangle"):
            base = input("Enter base ")
            base = int(base)
            height = input("Enter the height of the triangle: ")
            height = int(height)
            result = height/2 * base
            print(f'The area is {result:.6f}')
        elif(shape == "rectangle"):
            base = input("Enter base ")
            base = int(base)
            height = input("Enter the height of the rectangle: ")
            height = int(height)
            result = base * height
            print(f'The area is {result:.6f}')
        elif(shape == "circle"):
            radius = input("Enter the radius of the circle: ")
            radius = int(radius)
            result = math.pi * (radius * radius)
            print(f'The area is', result)
        elif(shape == ""):
            break
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
