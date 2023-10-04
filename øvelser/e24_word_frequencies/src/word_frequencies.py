#!/usr/bin/env python3

def word_frequencies(filename):
    res = {}
    f = open(filename, "r")
    lines = f.readlines()
    words = []
    for line in lines:
        lineWords = line.split(" ")
        for word in lineWords:
            char_string = """\!"#$%&'()*,./:;?@[]_"""
            word = word.strip(char_string)
            word = word.replace("\n", "")
            word = word.replace("-", " ")
            for char in char_string:
                word = word.replace(char, "")
            words.append(word)
    for word in words:
        if word in res.keys():
            res[word] += 1
        else:
            res.update({f'{word}':1})
    return res

def main():
    print(word_frequencies("src/alice.txt"))

if __name__ == "__main__":
    main()
