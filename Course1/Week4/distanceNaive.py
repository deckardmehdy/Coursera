# Uses python3
import math, itertools
import numpy as np

def calc_min_distance(X,Y,n,minDistance):
    x1,y1 = X[0],Y[0]
    for n in range(1,n):
        newDistance = math.hypot((x1 - X[i]),(y1 - Y[i]))
        if newDistance < minDistance:
            minDistance = newDistance
    return minDistance

# Record inputs: n; x and y coordinates
n = int(input())
x = np.zeros((n,1))
y = np.zeros((n,1))
for i in range(n):
    x[i],y[i] = [int(x) for x in input().split()]

# Calculate the euclidan distance
minDistance = math.hypot((x[0] - x[1]),(y[0] - y[1]))
if n > 2:
    for i in range(0,(n-1)):
        minDistance = calc_min_distance(x[i:n],y[i:n],(n-i),minDistance)
print(minDistance)
