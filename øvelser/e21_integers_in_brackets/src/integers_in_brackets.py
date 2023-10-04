#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    res = []
    pattern = r'\[[\s]*[\+\-]?[\d\s]+\]'
    mataches = re.findall(pattern, s)
    replace = ["[", "]", "+", " ", "\t"]
    for match in mataches:
        for char in replace:
            match = match.replace(char,"")
        res.append(int(match))
    return res

def main():
    print(integers_in_brackets("  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
