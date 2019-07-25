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

def makeTrie(n,patterns):
    # Create empty dict to store trie tree
    # Make the "0" the root node
    trie, nodeCount = {}, 1
    trie["0"] = [[],[]]
    
    # Loop through all patterns:
    for p in range(n):
        currentNode, pattern = 0, patterns[p]
        
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
                trie[str(nodeCount)] = [[letter],[]]
                currentNode = nodeCount
                nodeCount += 1

    # Returnt the trie tree at the end
    return trie

def printTrie(trie):
    # Create a FIFO queue and add the root node
    myQueue = queue.Queue()
    myQueue.put(0)

    # Go through all nodes in the trie tree
    # Adding and printing nodes as they are explored
    while myQueue.empty() != True:
        currentNode = myQueue.get()
        nextNodes = len(trie[str(currentNode)][1])
        if nextNodes > 0:
            for i in range(nextNodes):
                newNode = trie[str(currentNode)][1][i]
                newNodeLetter = trie[str(newNode)][0][-1]
                myQueue.put(newNode)
                print(str(currentNode) + "->" + str(newNode) + ":" + str(newNodeLetter))

################################
####### START OF PROGRAM #######
################################
n = int(input())

# Record patterns
patterns = [""] * n
for i in range(n):
    patterns[i] = str(input())


trie = makeTrie(n,patterns)
printTrie(trie)
