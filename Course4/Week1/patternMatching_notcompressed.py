# Runs using Python 3
import queue

def nextNode(trie,currentNode,letter):
    # See how many letters are in the node's adjanency list
    nextNodes = len(trie[str(currentNode)][1])
    
    # If there are none, then return None
    if nextNodes == 0:
        return None
    # If there are some, loop through and return if
    # the letter we are looking for is found:
    else:
        for i in range(nextNodes):
            nextNode = trie[str(currentNode)][1][i]
            if trie[str(nextNode)][0][-1] == letter:
                return trie[str(currentNode)][1][i]
        # If none of them match the letter, return None
        return None

def suffixTrie(text):
    # Create empty dict to store trie tree
    # Make the "0" the root node
    trie, nodeCount = {}, 1
    # Sub-list 0: letter corresponding to node;
    # Sub-list 1: next nodes numbers;
    # Sub-list 2: starting position within text of string
    trie["0"] = [[],[],[]]
    
    # Loop through all suffixs in text:
    T = len(text)
    for p in range(T):
        currentNode, pattern = 0, text[(0+p):T]
        
        # Go through each letter in each pattern
        for i in range(len(pattern)):
            letter = pattern[i]
            newNode = nextNode(trie,currentNode,letter)
            # If the letter exists in the adjacency list, then move onto the next one
            if newNode != None:
                currentNode = newNode
            # Otherwise, create a new node with the new letter
            # and append it to the current node's adacency list
            else:
                trie[str(currentNode)][1].append(nodeCount)
                trie[str(nodeCount)] = [[letter],[],[]]
                currentNode = nodeCount
                nodeCount += 1
            
            # If we are on the last letter in the pattern,
            # then append it to the list of starting vertexs
            if i == (len(pattern)-1):
                trie[str(currentNode)][2].append(p)

    # Returnt the trie tree at the end
    return trie

def findPatterns(trie,patterns):
    # Create a list to store pattern matches in text
    matches = []
    
    # Check all patterns:
    for p in range(len(patterns)):
        # See if we can match every letter in the pattern
        currentNode = 0
        pattern = patterns[p]
        matchFound = False
        
        for i in range(len(pattern)):
            letter = pattern[i]
            newNode = nextNode(trie,currentNode,letter)
            # If the letter exists in the adjacency list,
            # then move onto the next letter
            if newNode != None:
                currentNode = newNode
                # If all of the letters match,
                # then a match has been found
                if i == (len(pattern)-1):
                    matchFound = True
            # Otherwise, break out of the loop
            else:
                i = len(pattern)

        # If a match was found, add all of the starting
        # vertexs in the text to the list
        if matchFound == True:
            matches = findStartingPoints(trie,currentNode,matches)

    return matches

def findStartingPoints(trie,currentNode,matches):
    # Create a FIFO queue and make the current node the starting point
    myQueue = queue.Queue()
    myQueue.put(currentNode)
    
    # Go through all nodes in the trie tree, adding all of
    # the starting vertexs from the current node and beneath
    while myQueue.empty() != True:
        currentNode = myQueue.get()
        nextNodes = len(trie[str(currentNode)][1])
        startingVertexs = len(trie[str(currentNode)][2])
        if startingVertexs > 0:
            matches += trie[str(currentNode)][2]
        if nextNodes > 0:
            for j in range(nextNodes):
                newNode = trie[str(currentNode)][1][j]
                myQueue.put(newNode)

    return matches

################################
####### START OF PROGRAM #######
################################
text = str(input())
n = int(input())

# Record patterns
patterns = [""] * n
for i in range(n):
    patterns[i] = str(input())

# Make a suffex trie from the text
trie = suffixTrie(text)

# Find and print all of the matches of the pattern within the text
matches = findPatterns(trie,patterns)
if len(matches) == 0:
    print("")
else:
    matches.sort()
    print(*matches)
