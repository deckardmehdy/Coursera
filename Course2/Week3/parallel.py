# python3
import math
import numpy as np

def parent(i):
    return math.floor((i-1)/2)

def leftChild(i):
    return (2*i+1)

def rightChild(i):
    return (2*i+2)

def changePriority(threadHeap,threadIndex,job,n):
    threadHeap[0] = threadHeap[0] + job
    threadHeap,threadIndex = siftDown(threadHeap,threadIndex,0,n)
    return [threadHeap,threadIndex]

def siftDown(threadHeap,threadIndex,i,n):
    maxIndex = i
    l = leftChild(i)
    if l < n:
        if (threadHeap[l] < threadHeap[maxIndex]) or ((threadHeap[l] == threadHeap[maxIndex]) and (threadIndex[l] < threadIndex[maxIndex])):
            maxIndex = l
    r = rightChild(i)
    if r < n:
        if (threadHeap[r] < threadHeap[maxIndex]) or ((threadHeap[r] == threadHeap[maxIndex]) and (threadIndex[r] < threadIndex[maxIndex])):
            maxIndex = r
    if i != maxIndex:
        threadHeap[i],threadHeap[maxIndex] = threadHeap[maxIndex],threadHeap[i]
        threadIndex[i],threadIndex[maxIndex] = threadIndex[maxIndex],threadIndex[i]
        threadHeap,threadIndex = siftDown(threadHeap,threadIndex,maxIndex,n)
    return [threadHeap,threadIndex]

def assignJobs(threadHeap,threadIndex,jobs,m,n):
    for i in range(m):
        print(str(threadIndex[0]) + " " + str(threadHeap[0]))
        threadHeap,threadIndex = changePriority(threadHeap,threadIndex,jobs[i],n)

### START OF PROGRAM ###
n,m = [int(x) for x in input().split()]
jobs = [int(x) for x in input().split()]

# Create a min-heap that stores the threads and their total accumulated time
# Create a list which stores the thread index for a thread in the min-heap
threadHeap,threadIndex = [],[]
for i in range(n):
    threadHeap.append(0)
    threadIndex.append(i)

# Assign and print out jobs for each thread
assignJobs(threadHeap,threadIndex,jobs,m,n)
