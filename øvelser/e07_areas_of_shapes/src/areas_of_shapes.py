#!/usr/bin/env python3

import math


def main():
    form = " "

    def triangle(x,y):
        return int(x)*int(y)/2
    def rectangle(x,y):
        return int(x)*int(y)
    def circle(x):
        return math.pi*int(x)*int(x)

    while form != "":
        form=input("Choose a shape (triangle, rectangle, circle): ")
        if form == "triangle":
            x=input("Give base of the triangle: ")
            y=input("Give height of the triangle: ")
            print("The area is", triangle(x,y))
        elif form == "rectangle":
            x=input("Give width of the rectangle: ")
            y=input("Give height of the rectangle: ")
            print("The area is", rectangle(x,y))
        elif form == "circle":
            x=input("Give radius of the circle: ")
            print("The area is", circle(x))
        elif form == "":
            ''
        else:
            print("Unknown shape!")

    # enter you solution here

if __name__ == "__main__":
    main()
