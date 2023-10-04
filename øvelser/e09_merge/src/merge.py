#!/usr/bin/env python3

def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
 

def merge2(L1, L2):
    list = L1 + L2
    quickSort(list, 0, len(list)-1)
    return list

def merge(L1, L2):
    newlist = []
    extraList = []
    shortlist = []
    
    if len(L1) <= len(L2):
        shortlist += L1
        extraList += L2
    else: 
        shortlist += L2
        extraList += L1
    
    for x in range(len(shortlist)+1):
        delList = []
        for y in range(len(extraList)):
            if  x >= len(shortlist): 
                newlist.append(extraList[y])
            elif extraList[y] < shortlist[x]:
                newlist.append(extraList[y])
                delList.append(y)
        if not x >= len(shortlist): 
            newlist.append(shortlist[x])
        delList.reverse()
        for j in delList:
            del extraList[j]
    return newlist



def main():
    L1 = [-98, -59, -55, -54, -50, -48, -42, -33, -8, 7, 8, 14, 20, 37, 46, 49, 51, 56, 65, 84]
    L2 = [-61, -54, -51, -12, 1, 34, 40, 46, 72, 92]
    print(merge(L1, L2))
    L1 = [-86, -86, -77, -76, -70, -66, -63, -62, -46, -7, 11, 27, 30, 37, 51, 57, 67, 74, 89, 95]
    L2 =  [-71, -28, -17, 11, 53, 56, 57, 70, 90, 92]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()