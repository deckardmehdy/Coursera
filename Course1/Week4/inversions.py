# Uses python3
#import numpy as np
import math

def merge(B,C,inversions):
    D = []
    while (len(B) > 0) and (len(C) > 0):
        if B[0] <= C[0]:
            D.append(B[0])
            B.pop(0)
        else:
            D.append(C[0])
            C.pop(0)
            inversions = inversions + len(B)

    if len(B) > 0:
        D.extend(B)
    else:
        D.extend(C)
    return [D, inversions]

def merge_sort(array2sort,n,inversions):
    if n == 1:
        return [array2sort,inversions]
    m = int(math.floor(n/2))
    [B,inversionsB] = merge_sort(array2sort[0:m],m,inversions)
    [C,inversionsC] = merge_sort(array2sort[m:n],(n-m),inversions)
    inversions = inversionsB + inversionsC
    [A,inversions] = merge(B,C,inversions)
    return [A,inversions]

# Start of Function
n = int(input())
nums = [int(x) for x in input().split()]

# Sort the nums array with merge sort
[_,inversions] = merge_sort(nums,n,0)
print(inversions)




