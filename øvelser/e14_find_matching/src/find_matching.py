#!/usr/bin/env python3

def find_matching(List, pattern):
    return [
        i 
        for i, string in enumerate(List) 
        if pattern in string
        ]


def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "i"))

if __name__ == "__main__":
    main()
