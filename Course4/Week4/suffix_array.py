# Runs using Python 3

def sortCharacters(S):
    order = [0] * len(S)
    count = {"A": 0, "C": 0, "G": 0, "T": 0, "$": 0}
    chars = ["$", "A", "C", "G", "T"]
    for i in range(0,len(S)):
        count[str(S[i])] += 1
    for j in range(1,5):
        count[str(chars[j])] += count[str(chars[j-1])]
    for k in range((len(S)-1),-1,-1):
        c = S[k]
        count[str(c)] = count[str(c)] - 1
        order[count[str(c)]] = k
    return order

def computerCharClasses(S,order):
    Class = [0] * len(S)
    Class[order[0]] = 0
    for i in range(1,len(S)):
        if S[order[i]] != S[order[i-1]]:
            Class[order[i]] = Class[order[i-1]] + 1
        else:
            Class[order[i]] = Class[order[i-1]]
    return Class

def sortDoubled(S,L,order,Class):
    count = [0] * len(S)
    newOrder = [0] * len(S)
    for i in range(0,len(S)):
        count[Class[i]] += 1
    for j in range(1,len(S)):
        count[j] += count[j-1]
    for k in range((len(S)-1),-1,-1):
        start = (order[k] - L + len(S)) % len(S)
        cl = Class[start]
        count[cl] -= 1
        newOrder[count[cl]] = start
    return newOrder

def updateClasses(newOrder,Class,L):
    n = len(newOrder)
    newClass = [0] * n
    newClass[newOrder[0]] = 0
    for i in range(1,n):
        cur = newOrder[i]
        prev = newOrder[i-1]
        mid = cur + L
        midPrev = (prev + L) % n
        if (Class[cur] != Class[prev]) or (Class[mid] != Class[midPrev]):
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]
    return newClass

def buildSuffixArray(S):
    order = sortCharacters(S)
    Class = computerCharClasses(S,order)
    L = 1
    while L < len(S):
        order = sortDoubled(S,L,order,Class)
        Class = updateClasses(order,Class,L)
        L = 2 * L
    return order

################################
####### START OF PROGRAM #######
################################
T = str(input())
print(*buildSuffixArray(T))
