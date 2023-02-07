#!/usr/bin/env python3

def detect_ranges(lst):
  lst = sorted(lst)
  result = []
  start = lst[0]
  end = start
  for i in range(1, len(lst)):
    if lst[i] == lst[i-1] + 1:
      end = lst[i]
    else:
      if start == end:
        result.append(start)
      else:
        result.append((start, end+1))
      start = lst[i]
      end = start
  if start == end:
    result.append(start)
  else:
    result.append((start, end+1))
  return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
