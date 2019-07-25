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
    
    # Trie tree node structure:
        # Sub-list 0: [0] = starting index of string; [1] = length of string
        # Sub-list 1: indexs of next nodes
        # Sub-list 2: indexs within text of string
    trie["0"] = [[],[],[]]
    
    # Loop through all suffixs in text:
    T = len(text)
    for p in range(T):
        # Initialize starting node to root and starting pointer to index 0
        currentNode, pointer = 0, 0
        pattern = text[p:T]
        print("------------- New pattern " + str(pattern) + " -------------")
        
        while pointer < len(pattern):
            print("Pointer val is " + str(pointer))
            # See which nodes are stored in the adjacency list
            nextNodes = trie[str(currentNode)][1]
            print("Checking if any nodes exist in the current nodes AL...")
            
            # If there are nodes in the adjacency list:
            if len(nextNodes) > 0:
                print("Nodes exist! They are " + str(nextNodes))
                remainingString, matchIndex = pattern[pointer:len(pattern)], None
                print("Remaining string left in the pattern is " + str(remainingString))
                
                # Loop through all of the next nodes and see if any match the pattern:
                for i in range(len(nextNodes)):
                    # See if the next node's string match
                    nextNodeString = nodeString(trie,nextNodes[i],text)
                    print("Comparing " + str(remainingString) + " against " + str(nextNodeString) + "...")
                    if len(remainingString) > len(nextNodeString):
                        overlap = checkOverlap(remainingString,nextNodeString)
                        if overlap > 0:
                            matchIndex = i
                            i = len(nextNodes)                              # break out of loop
                    elif len(remainingString) < len(nextNodeString):
                        overlap = checkOverlap(nextNodeString,remainingString)
                        if overlap > 0:
                            matchIndex = i
                            i = len(nextNodes)                              # break out of loop
                    else:
                        # If they are the same length and match, then append the starting
                        # index of the pattern to the node's starting index list and
                        # move onto the next pattern
                        if remainingString == nextNodeString:
                            trie[str(currentNode)][2].append(nodeCount)
                            i, pointer = len(nextNodes), len(pattern)       # break out of loops
        
                # If any matches were found, split the matched node
                if matchIndex != None:
                    print("Match found between " + str(remainingString) + " and " + str(nextNodeString))
                    trie = insertNode(trie,currentNode,nodeCount,nextNodes[matchIndex],overlap,matchIndex)
                    nodeCount += 1
                    
                    # ADD NODE
                    # After adding the new node update the pointer and see if the pattern is finished:
                    pointer += overlap
                    
                    # If the pattern is finished, then append the start index to the new node's
                    if pointer == (len(pattern)-1):
                        trie[str(newNode)][2].append(p)
                
                # If no matches were found:
                else:
                    print("Creating a new node from node " + str(currentNode))
                    # Create a new node and update variables
                    trie = addNode(trie,currentNode,nodeCount,pointer,(len(pattern)-pointer),p)
                    nodeCount += 1
                    pointer = len(pattern)      # break out of loop
                    print(trie)
            
            # If there aren't any nodes in there:
            else:
                print("No nodes exist!")
                print("Creating a new node from node " + str(currentNode))
                # Create a new node and update variables
                trie = addNode(trie,currentNode,nodeCount,pointer,(len(pattern)-pointer),p)
                nodeCount += 1
                pointer = len(pattern)      # break out of loop
                print(trie)


    # Returnt the trie tree at the end
    return trie

def insertNode(trie,currentNode,newNode,nextNode,overlap,matchIndex): # NEED TO ADD A NODE AFTER
    # Change the current node's adjacency list
    trie[str(currentNode)][1][matchIndex] = newNode

    # Create a new intermediary node
    oldPointer = trie[str(nextNode)][0][0]
    trie[str(newNode)] = [[oldPointer,overlap],[nextNode],[]]

    # Change the next node's length and pointer
    newPointer = overlap + oldPointer
    newLength = trie[str(nextNode)][0][1] - overlap
    trie[str(nextNode)][0] = [newPointer,newLength]

    return trie

def addNode(trie,currentNode,newNode,pointer,length,startingIndex):
    trie[str(currentNode)][1].append(newNode)
    trie[str(newNode)] = [[pointer,length],[],[startingIndex]]
    return trie


def checkOverlap(largerString,smallerString):
    overlap, end = 0, False
    while (overlap < len(smallerString)) and (end == False):
        if smallerString[i] == largerString[i]:
            overlap += 1
        else:
            end == True
    return overlap

def nodeString(trie,nextNode,text):
    # Find starting and ending points of string for the next node,
    # construct it, and return it
    start = trie[str(nextNode)][0][0]
    end = start + trie[str(nextNode)][0][1]
    return text[start:end]

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
print(trie)
"""
# Find and print all of the matches of the pattern within the text
matches = findPatterns(trie,patterns)
if len(matches) == 0:
    print("")
else:
    matches.sort()
    print(*matches)
"""
