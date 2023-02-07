#!/usr/bin/env python3

def reverse_dictionary(d):
    rd = {}
    # for key, values in d.items():

    #     for v in values:
    #         rd[v] = []
        
    # for key, values in d.items():
    #     for v in values:
    #         rd[v].append(key)

    for key, values in d.items():
        for v in values:
            if v not in rd.keys():
                rd[v] = [key]
            else:
                rd[v] += [key]

    return rd

def main():
    pass

if __name__ == "__main__":
    main()
