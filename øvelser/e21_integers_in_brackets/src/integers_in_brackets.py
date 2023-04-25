#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    regex = r"\[\s*([+-]?\d+)\s*\]"
    m = re.findall(regex, s)
    return [int(tal)for tal in m]

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))


if __name__ == "__main__":
    main()
