#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    with open("src/rgb.txt", "r") as f:
        data = f.readlines()
    # remove the first line
    data = data[1:]
    cleaned_data = []
    # use regular expressions to clean up the data
    for line in data:
        match = re.search(r"(\d+)\s+(\d+)\s+(\d+)\s+(.+)", line)
        red = match.group(1)
        green = match.group(2)
        blue = match.group(3)
        name = match.group(4)
        cleaned_data.append(f"{red}\t{green}\t{blue}\t{name}")
    return cleaned_data

def main():
    print(red_green_blue)

if __name__ == "__main__":
    main()
