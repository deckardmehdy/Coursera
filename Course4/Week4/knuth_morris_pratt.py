# Runs using Python 3

def computePrefixFunction(P):
    s = [0] * len(P)
    border = 0
    for i in range(1,len(P)):
        while (border > 0) and (P[i] != P[border]):
            border = s[border-1]
        if P[i] == P[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s

def findAllOccurrences(P,T):
    S = P + "$" + T
    s = computePrefixFunction(S)
    result = []
    for i in range((len(P)+1),len(S)):
        if s[i] == len(P):
            result.append(i-(2*len(P)))
    return result

################################
####### START OF PROGRAM #######
################################
P = str(input())
T = str(input())
if len(P) > len(T):
    print()
else:
    result = findAllOccurrences(P,T)
    if len(result) > 0:
        print(*result)
    else:
        print()
