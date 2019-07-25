# Runs using Python 3

class SuffixTree:
    class Node:
        # Node constructor:
        def __init__(self,starting_index,length):
            self.starting_index = starting_index
            self.length = length
            self.children = []
            self.marker = None

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
    
        # Change parameters of the old node
        node.children = [newNode]
        node.length = node.length - new_length
    
        
    def add_child(self,node,starting_index,length):
        newNode = self.Node(starting_index,length)
        node.children.append(newNode)
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
                        if charsLeft > 0:
                            node = children[i]
                        pointer += overlap
                            
                    # If the entire child's string wasn't matched,
                    # split the current node:
                    else:
                        mySuffixTree.divide(children[i],overlap)
                        # If the suffix isn't finished, add a new
                        # node with the remaining suffix:
                        if charsLeft > 0:
                            newNode = mySuffixTree.add_child(children[i],(pointer+overlap),charsLeft)
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

def pathTo(node,stack,text,type):
    str = ""
    if type == "leaf":
        i = len(stack) - 2
    else:
        i = len(stack) - 1

    while i > 0:
        node = stack[i]
        str = nodeString(node,text) + str
        i -= 1
    return str

def findPoundSym(string):
    for i in range(len(string)):
        if string[i] == "#":
            return [i,True]
    return [None,False]

def allChildrenMarked(node,stack):
    parent = stack[-2]
    parentsChildren = parent.children
    for i in range(len(parentsChildren)):
        sibling = parentsChildren[i]
        if (sibling != node) and (sibling.marker == None):
            return False
    return True

def childrenMark(node,stack):
    parent = stack[-2]
    parentsChildren = parent.children
    for i in range(len(parentsChildren)):
        sibling = parentsChildren[i]
        if (sibling != node) and (sibling.marker == "R"):
            return "R"
    return "L"

def swapParentsChildren(node,stack):
    parent = stack[-2]
    parentsChildren = parent.children
    for i in range(len(parentsChildren)):
        if parentsChildren[i] == node:
            parentsChildren[-1], parentsChildren[i] = parentsChildren[i], parentsChildren[-1]

def getUniqueStrings(text1,text,tree):
    # Create a stack with the root on top
    stack = [tree.root]
    # Initialize result to longest possible unique sequence
    result = text1

    # Do a DFS of the tree
    while len(stack) > 0:
        # Peek at the top of the stack
        #print("Stack length: " + str(len(stack)))
        node = stack[-1]
        children = node.children
        
        # See if the node is a leaf or non-leaf node:
        if len(children) > 0:             # Non-leaf
            # Check if any leaves aren't marked
            i, leafMarkings = 0, "L"
            while i < len(children):
                #print("Entering child loop...")
                child = children[i]
                # If one isn't, then put it on top of the stack
                if child.marker == None:
                    #print("Child with string " + nodeString(child,text) + " being added to top of stack")
                    stack.append(child)
                    i = len(children)+1          # break from loop & set flag
                else:
                    i += 1
                    if child.marker == "R":
                        leafMarkings = "R"
        
            # All leaves have been marked:
            if i != (len(children)+1):
                #print("Entering all leaves marked loop...")
                if (leafMarkings == "L"):
                    node.marker = "L"
                    newResult = pathTo(node,stack,text,"non-leaf")
                    #print("Node with string " + nodeString(node,text) + " has just been marked with L!")
                    #print("String from root to node is " + newResult)
                    if len(newResult) < len(result):
                        result = newResult
                #print("Result has been updated to " + str(result))
                else:
                    node.marker = "R"
                _ = stack.pop()
                    #print("Stack was just popped!")
    
        else:                               # Leaf
            [index,found] = findPoundSym(nodeString(node,text))
            if (found == True) and (index > 0):            # see if this statement is valid
                node.marker = "L"
                string = nodeString(node,text)
                newResult = pathTo(node,stack,text,"leaf") + string[0]
                #print("Node with string " + nodeString(node,text) + " has just been marked with L!")
                #print("String from root to node is " + newResult)
                if len(newResult) < len(result):
                    result = newResult
            #print("Result has been updated to " + str(result))
            # Special case: if all parents leaves are L and leaf starts with '#'
            elif (found == True) and (index == 0) and (len(stack) > 2):
                # Check if all of its parent's children have been marked:
                if allChildrenMarked(node,stack) == True:
                    # Check if all children have a mark 'L'
                    if childrenMark(node,stack) == "L":
                        node.marker = "L"
                        string = nodeString(node,text)
                        newResult = pathTo(node,stack,text,"leaf")
                        #print("Node with string " + nodeString(node,text) + " has just been marked with L!")
                        #print("String from root to node is " + newResult)
                        if len(newResult) < len(result):
                            result = newResult
                    #print("Result has been updated to " + str(result))
                    else:
                        node.marker = "R"
            #print("Node with string " + nodeString(node,text) + " has just been marked with R!")
                # If they haven't been checked, then put this node
                # at the end of the parents children
                else:
                    swapParentsChildren(node,stack)
        #print("Node being swapped...")
            else:
                node.marker = "R"
            #print("Node with string " + nodeString(node,text) + " has just been marked with R!")
            _ = stack.pop()

    return result

################################
####### START OF PROGRAM #######
################################
text1 = str(input())
text2 = str(input())
text = text1 + "#" + text2 + "$"

# Make a suffex tree from the text
tree = suffixTree(text)

# Print trie tree
print(getUniqueStrings(text1,text,tree))
