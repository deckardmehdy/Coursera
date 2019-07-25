# python3
import math

def parent(i):
    return math.floor((i-1)/2)

def leftChild(i):
    return (2*i+1)

def rightChild(i):
    return (2*i+2)

def siftDown(nums,i,n):
    global swaps,swapCount
    maxIndex = i
    l = leftChild(i)
    if (l < n) and (nums[l] < nums[maxIndex]):
        maxIndex = l
    r = rightChild(i)
    if (r < n) and (nums[r] < nums[maxIndex]):
        maxIndex = r
    if i != maxIndex:
        nums[i],nums[maxIndex] = nums[maxIndex],nums[i]
        swaps.append([i,maxIndex])
        swapCount += 1
        nums = siftDown(nums,maxIndex,n)
    return nums

def buildHeap(nums,n):
    for i in range(math.floor((n-1)/2), -1, -1):
        nums = siftDown(nums,i,n)

### START OF PROGRAM ###
n = int(input())
nums = [int(x) for x in input().split()]

swaps, swapCount = [], 0
buildHeap(nums,n)

print(swapCount)
if swapCount > 0:
    for i in range(swapCount):
        print(str(swaps[i][0]) + " " + str(swaps[i][1]))
