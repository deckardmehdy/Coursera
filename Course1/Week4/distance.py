# Uses python3
import math, itertools
import numpy as np

# Record inputs: n; x and y coordinates
n = int(input())
x = np.zeros((n,1))
y = np.zeros((n,1))
for i in range(n):
    x[i],y[i] = [int(x) for x in input().split()]

# Create the combintations of X and Y
combosX = list(itertools.combinations(x,r=2))
combosY = list(itertools.combinations(y,r=2))

# Calculate the euclidan distance
minDistance = math.hypot((combosX[0][0] - combosX[0][1]),(combosY[0][0] - combosY[0][1]))
if n > 2:
    for i in range(1,len(combosX)):
        newDistance = math.hypot((combosX[i][0] - combosX[i][1]),(combosY[i][0] - combosY[i][1]))
        if newDistance < minDistance:
            minDistance = newDistance
print(minDistance)
