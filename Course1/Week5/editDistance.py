# Uses python3
import numpy as np

def calc_optimal_distance(string1,n,string2,m,D):
    for j in range (1,m+1):
        for i in range (1,n+1):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            mismatch = D[i-1][j-1] + 1
            match = D[i-1][j-1]
            if string1[i-1] == string2[j-1]:
                D[i][j] = min(insertion,deletion,match)
            else:
                D[i][j] = min(insertion,deletion,mismatch)
    return D[n][m]

### START OF FILE: ###
# Get integers n and m and their sequences
string1 = str(input())
string2 = str(input())

# Get lengths of strings
n,m = len(string1), len(string2)

# Create 2-D distance array and add 1s to left-hand and upper border
D = np.zeros(((n+1),(m+1)),dtype=int)

for i in range(n+1):
    D[i][0] = i
for j in range(m+1):
    D[0][j] = j

# Calc optimal distance
print(calc_optimal_distance(string1,n,string2,m,D))

