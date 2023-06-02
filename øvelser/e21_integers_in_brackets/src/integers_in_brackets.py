#!/usr/bin/env python3
import re;

def integers_in_brackets(s):
    L = []
    pattern = r"\[\s*([+-]?\d*)\s*\]"
    for i in re.findall(pattern, s):
        res = (int(i))
        L.append(res)
    return L

def main():
    integers_in_brackets(' afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx')
    pass

if __name__ == "__main__":
    main()
