# python3
import numpy as np
import random

def polyHash(S,p,x):
    hash = 0
    for i in range((len(S)-1),-1,-1):
        code = ord(S[i])
        hash = ((hash * x) + code) % p
    return hash

def precomputeHashes(T,patternLen,p,x):
    textLen = len(T)
    H = np.zeros(((textLen - patternLen + 1)), dtype=int)
    S = T[(textLen - patternLen):textLen]
    H[(textLen - patternLen)] = polyHash(S,p,x)
    y = 1
    for i in range(1,(patternLen+1)):
        y = (y * x) % p
    for i in range((textLen - patternLen - 1), -1, -1):
        H[i] = ((x * H[(i+1)]) + ord(T[i]) - (y * ord(T[i + patternLen]))) % p
    return H

def rabinKarp(T,P):
    p, patternLen = 1000003, len(P)
    x = random.randint(1,p)
    result = []
    pHash = polyHash(P,p,x)
    H = precomputeHashes(T,patternLen,p,x)
    for i in range(len(T) - patternLen + 1):
        if pHash == H[i]:
            if P == T[i:(i+patternLen)]:
                result.append(i)
    return result

### START OF PROGRAM ###
P = str(input())
T = str(input())

# Find indices that the pattern occurs in the text
result = rabinKarp(T,P)
numOfIndices = len(result)

# Print the indicies
if numOfIndices > 0:
    strOfIndices = str(result[0])
    for i in range(1,numOfIndices):
        strOfIndices += " " + str(result[i])
    print(strOfIndices)
else:
    print("")
