#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    res =[]
    pattern = r'\w+(?:\w+)*'
    f = open(filename, "r")
    lines = f.readlines()
    del lines[0]
    for line in lines:
        matches = re.findall(pattern, line)
        ans = ""
        for match in matches[:3]:
            ans += f"{match}\t"
        for match in matches[3:]:
            ans += f"{match} "
        ans = ans[:-1]
        res.append(ans)
    
    return res


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
