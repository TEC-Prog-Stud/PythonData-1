#!/usr/bin/env python3

def word_frequencies(filename):
    res = {}
    f = open(filename, "r")
    lines = f.readlines()
    words = []
    for line in lines:
        lineWords = line.split()
        for word in lineWords:
            word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
            words.append(word)
    for word in words:
        if word in res.keys():
            res[word] += 1
        else:
            res.update({f'{word}':1})
    f.close()
    return res

def main():
    print(word_frequencies("src/alice.txt"))

if __name__ == "__main__":
    main()
