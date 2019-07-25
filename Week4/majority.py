# Uses python3
#import numpy as np
import math

def merge(B,C):
    D = []
    while (len(B) > 0) and (len(C) > 0):
        if B[0] <= C[0]:
            D.append(B[0])
            B.pop(0)
        else:
            D.append(C[0])
            C.pop(0)

    if len(B) > 0:
        D.extend(B)
    else:
        D.extend(C)
    return D

def merge_sort(array2sort,n):
    if n == 1:
        return array2sort
    m = int(math.floor(n/2))
    B = merge_sort(array2sort[0:m],m)
    C = merge_sort(array2sort[m:n],(n-m))
    A = merge(B,C)
    return A

def find_majority(sorted_nums,n):
    count,currentNum,majority = 0,0,(n/2)
    for i in range(n):
        if currentNum != sorted_nums[i]:
            count = 1
            currentNum = sorted_nums[i]
        else:
            count = count + 1
            if count > majority:
                return 1
    return 0

# Start of Function
n = int(input())
nums = [int(x) for x in input().split()]

# Sort the nums array with merge sort
sorted_nums = merge_sort(nums,n)

# See if majority exists
print(find_majority(sorted_nums,n))



