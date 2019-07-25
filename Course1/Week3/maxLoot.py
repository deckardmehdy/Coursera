# Uses python3
import numpy as np

def maxLoot(items,numOfItems,W):
    maxLoot = 0
    for i in range(numOfItems):
        if W == 0:
            return maxLoot
        else:
            currentItemWeight = items[i][1]
            if currentItemWeight <= W:
                W = W - currentItemWeight
                maxLoot = maxLoot + items[i][0]
            else:
                maxLoot = maxLoot + (W * items[i][2])
                W = 0
    return maxLoot


# Start of Function
numOfItems, W = [int(x) for x in input().split()]
items = np.zeros((numOfItems,3))
for i in range(numOfItems):
    a,b = [int(x) for x in input().split()]
    items[i][0], items[i][1],items[i][2] = a,b,(a/b)
if numOfItems > 1:
    items = sorted(items,reverse = True, key=lambda item: item[2])
print(maxLoot(items,numOfItems,W))

