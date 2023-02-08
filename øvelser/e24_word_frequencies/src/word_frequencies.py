#!/usr/bin/env python3

import string

def word_frequencies(filename):
    with open(filename, "r") as f:
        data = f.read()
    words = data.split()
    words = [word.strip(string.punctuation) for word in words]
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def main():
    freq = word_frequencies("alice.txt")
    for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
