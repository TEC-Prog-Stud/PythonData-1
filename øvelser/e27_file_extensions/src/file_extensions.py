#!/usr/bin/env python3

import re
import sys

def file_extensions(filename):
    f = open(filename, "r")
    lines = f.readlines()
    pattern = r'\.[^.\s]*$'

    matches = []
    for line in lines:
        match = re.search(pattern, line)
        match = match.group().replace(".","") if match is not None else match
        matches.append(match)
    dictionary = {}
    rest = []
    for match in matches:
        if match is not None:
          values = list(word.strip("\n") for word in (line for line in lines if match in line))
          dictionary[match] = values
        else:
          values = list(word.strip("\n") for word in ((line for line in lines if "." not in line)))
          rest = values
    f.close()
    
    return (rest, dictionary)

def main():
    ans = file_extensions("src/filenames.txt")
    print(f"{len(ans[0])} files with no extension")
    for key in sorted(ans[1].keys()):
         print(f"{key} {len(ans[1][key])}")
    # for arg in sys.argv[1:]:
    #   ans = file_extensions(arg)
    #   print(f"{len(ans[0])} files with no extension")
    #   for key in sorted(ans[1].keys()):
    #      print(f"{key} {len(ans[1][key])}")

if __name__ == "__main__":
    main()
