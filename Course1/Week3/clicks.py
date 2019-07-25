# Uses python3
import numpy as np

# Start of Function
ads = int(input())
A = np.sort([int(x) for x in input().split()])
B = np.sort([int(x) for x in input().split()])
B = np.reshape(B,(ads,1))
print(int(np.dot(A,B)))


