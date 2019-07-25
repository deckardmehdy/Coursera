# python3

def polyHash(S,p,x,m):
    hash = 0
    for i in range((len(S)-1),-1,-1):
        code = ord(S[i])
        hash = ((hash * x) + code) % p
    return (hash % m)

def findString(hashTable,hash,S,returnIndex = False):
    entries = len(hashTable[hash])
    for i in range(entries):
        if hashTable[hash][i] == S:
            if returnIndex == False:
                return True
            else:
                return i
    if returnIndex == False:
        return False
    else:
        return -1

### START OF PROGRAM ###
m = int(input())
p,x = 1000000007,263

# Create the hash table
hashTable = []
for i in range(m):
    hashTable.append([])

N = int(input())
for i in range(N):
    request = [str(x) for x in input().split()]
    if request[0] == "add":                                         # Add:
        hash = polyHash(request[1],p,x,m)                               # Find the string's hash code
        if findString(hashTable,hash,request[1]) == False:              # If the string doesn't exist,
            hashTable[hash].append(request[1])                          # append it to the end of the list
    elif request[0] == "del":                                       # Delete:
        hash = polyHash(request[1],p,x,m)                               # Find the string's hash code
        i = findString(hashTable,hash,request[1], returnIndex = True)  # Find the string's index in HT
        if i > -1:                                                  # If the string exists, delete it
            hashTable[hash].pop(i)
    elif request[0] == "find":                                      # Find:
        hash = polyHash(request[1],p,x,m)                               # Find the string's hash code
        if findString(hashTable,hash,request[1]) == True:               # If the string exists, print "yes"
            print("yes")
        else:                                                           # If it doesn't, print "no"
            print("no")
    else:                                                           # Check:
        entries = len(hashTable[int(request[1])])
        if entries > 0:
            outputString = hashTable[int(request[1])][(entries-1)]
            for i in range((entries-2),-1,-1):
                outputString = outputString + " " + hashTable[int(request[1])][i]
            print(outputString)
        else:
            print("")

