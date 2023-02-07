#!/usr/bin/env python3

def distinct_characters(list):
    result = {}
    for word in list:
        result[word] = len(set(word))
    return result

def main():
    print(distinct_characters(["check", "look", "try", "pop", "Hallo"]))

if __name__ == "__main__":
    main()
