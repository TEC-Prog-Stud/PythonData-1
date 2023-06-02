#!/usr/bin/env python3


def word_frequencies(filename=r'src/alice.txt'):
    frequencies = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                # word = word.lower #This doesn't work in test

                frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

def main():
    wordlist = word_frequencies(r'C:\Users\TEC\PythonData-1\PythonData-1\øvelser\e24_word_frequencies\src\alice.txt')
    print(wordlist)
    for word, count in wordlist.items():
        print(f"{word}\t{count}")
    pass

if __name__ == "__main__":
    main()
