#!/usr/bin/env python3

def reverse_dictionary(d):
    reverse_dict = {}
    for key, value in d.items():
        for item in value:
            if item not in reverse_dict:
                reverse_dict[item] = [key]
            else:
                reverse_dict[item].append(key)
    return reverse_dict

def main():
    print(reverse_dictionary({'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}))

if __name__ == "__main__":
    main()
