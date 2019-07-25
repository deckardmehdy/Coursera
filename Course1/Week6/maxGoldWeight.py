# python3
import numpy as np

def findMaxWeight(W,n,goldBars):
    value = np.zeros(((W+1),(n+1)), dtype=int)
    for i in range(1,(n+1)):
        for w in range(1,(W+1)):
            value[w,i] = value[w,(i-1)]
            if goldBars[i-1] <= w:
                    val = value[(w-goldBars[i-1]),(i-1)] + goldBars[i-1]
                    if value[w,i] < val:
                        value[w,i] = val
    return value[W,n]


### START OF PROGRAM ###
W, n = [int(x) for x in input().split()]
goldBars = [int(x) for x in input().split()]
print(findMaxWeight(W,n,goldBars))
