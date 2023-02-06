#!/usr/bin/env python3

import math


def main():

    loop = True
    while loop:
        shape = input("Enter shape(triangle/rectangle/circle): ")
        if shape == "":
            loop = False
        elif shape == "triangle":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = 0.5 * base * height
            if result:
                print("The area is {:.6f}".format(result))
        elif shape == "rectangle":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = width * height
            if result:
                print("The area is {:.6f}".format(result))
        elif shape == "circle":
            radius = float(input("Enter radius: "))
            result = math.pi * radius ** 2
            if result:
                print("The area is {:.6f}".format(result))
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
