# Uses python3
import numpy as np

def calc_optimal_distance(A,n,B,m,D):
    for j in range (1,m+1):
        for i in range (1,n+1):
            deletion1 = D[i][j-1]
            deletion2 = D[i-1][j]
            mismatch = D[i-1][j-1]
            match = D[i-1][j-1] + 1
            if A[i-1] == B[j-1]:
                D[i][j] = max(deletion1,deletion2,match)
            else:
                D[i][j] = max(deletion1,deletion2,mismatch)
    return D[n][m]

### START OF FILE: ###
# Get integers n and m and their sequences
n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
B = [int(x) for x in input().split()]

# Create 2-D distance array
D = np.zeros(((n+1),(m+1)),dtype=int)

# Calc optimal distance
print(calc_optimal_distance(A,n,B,m,D))
