#!/usr/bin/env python3

def word_frequencies(filename = "src/alice.txt"):
    with open(filename, "r") as f:
        data = f.read()
    words = data.split()
    words = [word.strip("""!"#$%&'()*,-./:;?@[]_""") for word in words]
    uwords = set(words)
    
    word_frekvens = {word: 0 for word in uwords}
    for word in words:
        word_frekvens[word] += 1
    return word_frekvens

def main():
    frekenvs = word_frequencies(r'PythonData-1\øvelser\e24_word_frequencies\src\alice.txt')
    for word, count in sorted(frekenvs.items(), key=lambda value: value[1], reverse=True):
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
