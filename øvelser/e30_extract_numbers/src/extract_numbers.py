#!/usr/bin/env python3

def extract_numbers(s):
    words = s.split()
    res = []
    for word in words:
        ans = tryConvert(word)
        if ans:
            res.append(ans)
            
    return res

def tryConvert(s):
    try:
        ans = int(s)
        return ans
    except Exception:
        try:
            ans = float(s)
            return ans
        except Exception:
            return None

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
