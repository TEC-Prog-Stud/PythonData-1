#!/usr/bin/env python3
import math

# class Rational(object):
#     def __init__(self, num1, num2) -> None:
#         self.rat = num1 / num2
#         self.data = [num1, num2]
    
#     def __str__(self):
#         return f"{self.data[0]}/{self.data[1]}"

#     def __add__(self, o) -> float:
#         return self.rat + o.rat
    
#     def __sub__(self, o) -> float:
#         return self.rat - o.rat
    
#     def __mul__(self, o) -> float:
#         return self.rat * o.rat
    
#     def __truediv__(self, o) -> float:
#         return self.rat / o.rat
    
#     def __eq__(self, o) -> bool:
#         return self.rat == o.rat
    
#     def __gt__(self, o) -> bool:
#         return self.rat > o.rat
    
#     def __lt__(self, o) -> bool:
#         return self.rat < o.rat
    
#     def __getitem__(self, index):
#         return self.data[index]

class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __add__(self, other):
        if isinstance(other, Rational):
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Rational):
            new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError("Division by zero")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for /")

    def __lt__(self, other):
        if isinstance(other, Rational):
            return (self.numerator * other.denominator) < (other.numerator * self.denominator)
        else:
            raise TypeError("Unsupported operand type for <")

    def __gt__(self, other):
        if isinstance(other, Rational):
            return (self.numerator * other.denominator) > (other.numerator * self.denominator)
        else:
            raise TypeError("Unsupported operand type for >")

    def __eq__(self, other):
        if isinstance(other, Rational):
            return (self.numerator == other.numerator) and (self.denominator == other.denominator)
        else:
            return False

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
