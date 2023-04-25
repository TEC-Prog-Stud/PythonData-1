#!/usr/bin/env python3

def word_frequencies(filename="src/alice.txt"):
    L = []
    with open(filename, "r") as f:
        alice = f.read()
    
    words = alice.split()
    words = [w.strip("""!"#$%&'()*,-./:;?@[]_""") for w in words]

    print(len(words))
    uWords = set(words)
    print(len(uWords))

    wd = {
        w:0 for w in uWords
    }

    for w in words:
        wd[w] +=1

    wd = dict(sorted(wd.items(), key=lambda x: x[1], reverse=True))


    return wd

def main():
    print(word_frequencies(r'øvelser\e24_word_frequencies\src\alice.txt'))


if __name__ == "__main__":
    main()
