#!/usr/bin/env python3

# Write function `integers_in_brackets` that finds from a given string all integers that are enclosed in brackets.

# Example run:
# `integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx")`
# returns
# `[12, -43, 12]`.
# So there can be whitespace between the number and the brackets, but no other character besides those that make up the integer.

# Test your function from the `main` function.


import re


def integers_in_brackets(s):
    
    regex = r"\[\s?([+-]?\d+)\s?\]"
    m = re.findall(regex, s)
    return [int(tal) for tal in m]

def main():
    print(integers_in_brackets("afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
