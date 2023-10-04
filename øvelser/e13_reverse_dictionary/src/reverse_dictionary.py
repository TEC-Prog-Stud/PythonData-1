#!/usr/bin/env python3

def reverse_dictionary(d : dict):
    res = {}
    for key in d:
        for value in d[key]:
            if value in res.keys():
                res[value].append(key)
            else:
                res[value] = [key]
    return res

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))
    

if __name__ == "__main__":
    main()
