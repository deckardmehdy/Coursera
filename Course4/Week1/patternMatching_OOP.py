# Runs using Python 3
import queue, copy

class SuffixTree:
    class Node:
        # Node constructor:
        def __init__(self,starting_index,length):
            self.starting_index = starting_index
            self.length = length
            self.children = []
            #self.starting_vertices = []
            #self.ID = None

    # Suffix Tree constructor:
    def __init__(self):
        self.root = None

    def divide(self,node,splitting_index):
        # Create a new node
        new_length = node.length - splitting_index
        new_pointer = node.starting_index + splitting_index
        newNode = self.Node(new_pointer,new_length)
        
        # Transfer over the old pointers and parameters
        # to the new node
        newNode.children = node.children
        #newNode.starting_vertices = copy.deepcopy(node.starting_vertices)
    
        # Change parameters of the old node
        node.children = [newNode]
        #node.starting_vertices = []
        node.length = node.length - new_length
    
        
    def add_child(self,node,starting_index,length):
        newNode = self.Node(starting_index,length)
        node.children.append(newNode)
        #newNode.starting_vertices.append(SI)
        #node.starting_vertices.append(SI)
        return newNode

def suffixTree(text):
    # Create a suffix tree object and make a root node
    mySuffixTree = SuffixTree()
    root = mySuffixTree.Node(None,None)
    mySuffixTree.root = root

    # Go through all suffixs in text and add them to the tree:
    for s in range(len(text)):
        suffix = text[s:len(text)]
        node, pointer = root, s
        while pointer < len(text):
            children, found, i = node.children, False, 0
            while i < len(children):
                childString = nodeString(children[i],text)
                remainingSuffix = text[pointer:len(text)]
                overlap = checkOverlap(remainingSuffix,childString)
                # If we do find a match:
                if overlap > 0:
                    charsLeft = len(text) - (pointer + overlap)
                    
                    # If the entire child's string was matched:
                    if overlap == len(childString):
                        #children[i].starting_vertices.append(s)
                        #node.starting_vertices.append(s)
                        if charsLeft > 0:
                            node = children[i]
                        pointer += overlap
                            
                    # If the entire child's string wasn't matched,
                    # split the current node:
                    else:
                        mySuffixTree.divide(children[i],overlap)
                        #children[i].starting_vertices.append(s)
                        # If the suffix isn't finished, add a new
                        # node with the remaining suffix:
                        if charsLeft > 0:
                            newNode = mySuffixTree.add_child(children[i],(pointer+overlap),charsLeft)
                        #else:
                            #children[i].starting_vertices.append(s)
                        pointer = len(text)
                    i, found = len(children), True
                else:
                    i += 1
                        
            # If no children were found that match the suffix,
            # then add a new child with the remaining suffix
            if found == False:
                length = len(text) - pointer
                newNode = mySuffixTree.add_child(node,pointer,length)
                pointer += length

    return mySuffixTree

def checkOverlap(suffixString,nodeString):
    overlap, j = 0, 0
    minRange = min(len(suffixString),len(nodeString))
    while j < minRange:
        if suffixString[j] == nodeString[j]:
            overlap += 1
            j += 1
        else:
            j = minRange
    return overlap

def nodeString(node,text):
    start = node.starting_index
    end = node.length + start
    return text[start:end]

def printTrie(mySuffixTree,text):
    # Create a FIFO queue and add the root node
    myQueue = queue.Queue()
    myQueue.put(mySuffixTree.root)
    #nodeCount = 0
    #mySuffixTree.root.ID = nodeCount
    #nodeCount += 1
    
    # Go through all nodes in the trie tree, adding and printing nodes as they are explored
    while myQueue.empty() != True:
        node = myQueue.get()
        nextNodes = len(node.children)
        for i in range(nextNodes):
            newNode = node.children[i]
            #newNode.ID = nodeCount
            #nodeCount += 1
            newNodeString = nodeString(newNode,text)
            myQueue.put(newNode)
            #print(str(node.ID) + "->" + str(newNode.ID) + ":" + str(newNodeString))
            print(newNodeString)

def getStartingVertices(node,mySuffixTree,indexs):
    startingVertices = node.starting_vertices
    for i in range(len(startingVertices)):
        indexs[startingVertices[i]] += 1
    return indexs

def findPatterns(mySuffixTree,patterns,text):
    indexs = [0] * len(text)

    for p in range(len(patterns)):
        pointer, pattern = 0, patterns[p]
        node = mySuffixTree.root
        while pointer < len(patterns[p]):
            children, i, found = node.children, 0, False
            while i < len(children):
                child = children[i]
                childString = nodeString(child,text)
                remainingPattern = pattern[pointer:len(pattern)]
                overlap = checkOverlap(remainingPattern,childString)
                if overlap == 0:
                    i += 1
                else:
                    found = True
                    charsLeft = len(pattern) - (pointer + overlap)
                    if charsLeft == 0:
                        # Pattern found:
                        indexs = getStartingVertices(child,mySuffixTree,indexs)
                        i = len(children)
                        pointer = len(pattern)
                    else:
                        # Continue searching for pattern:
                        if overlap == len(childString):
                            node = child
                            pointer += overlap
                            i = len(children)
                        # Pattern not found in text:
                        else:
                            i = len(children)
                            pointer = len(pattern)
    
            # Pattern not found in text:
            if found == False:
                pointer = len(pattern)

    return indexs

def sortedIndexs(indexs):
    list = []
    for i in range(len(indexs)):
        if indexs[i] > 0:
            list += [i] * indexs[i]
    return list

################################
####### START OF PROGRAM #######
################################
text = str(input())
"""
n = int(input())

# Record patterns
patterns = [""] * n
for i in range(n):
    #patterns[i] = str(input())
"""
# Make a suffex tree from the text
tree = suffixTree(text)

# Print trie tree
printTrie(tree,text)

# Go through and print all occurances of patterns in text
"""
indexs = findPatterns(tree,patterns,text)
if len(indexs) == 0:
    print("")
else:
    print(*sortedIndexs(indexs))
"""
