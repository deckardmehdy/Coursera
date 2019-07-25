# python3
import copy

def inOrderTraversal(tree):
    inOrderList, stack = [], [0]
    
    # Traverse all nodes in tree
    while len(stack) != 0:
        # Peek at the top of the stack
        node = stack[-1]
        
        # See the left and right childen and if they were visited
        leftChild, leftChildVisited = tree[str(node)][1], tree[str(node)][2]
        rightChild = tree[str(node)][3]

        # If the left child is valid and it hasn't been visited,
        # then add it to the top of the stack and visit it
        if (leftChild != -1) and (leftChildVisited == False):
            stack.append(leftChild)
            tree[str(node)][2] = True
        # Otherwise, append the current node to the In Order list
        else:
            inOrderList.append(tree[str(stack.pop())][0])
            # If it has a right child, then add that to the top of the stack
            if rightChild != -1:
                stack.append(rightChild)

    return inOrderList

def preOrderTraversal(tree):
    preOrderList, stack, alreadyStored = [], [0], False
    
    # Traverse all nodes in tree
    while len(stack) != 0:
        # Peek the top of the stack
        node = stack[-1]
        
        # Append it to the pre order list if it hasn't been stored already
        # and reset the flag
        if alreadyStored == False:
            preOrderList.append(tree[str(node)][0])
        alreadyStored = False
        
        # See the left and right childen and if they were visited
        leftChild, leftChildVisited = tree[str(node)][1], tree[str(node)][2]
        rightChild, rightChildVisited = tree[str(node)][3], tree[str(node)][4]
        
        # If the left child is valid and it hasn't been visited,
        # then add it to the top of the stack and visit it
        if (leftChild != -1) and (leftChildVisited == False):
            stack.append(leftChild)
            tree[str(node)][2] = True
        # Otherwise, if the right child is valid and it hasn't been visited,
        # then add that to the top of the stack
        elif (rightChild != -1) and (rightChildVisited == False):
                stack.append(rightChild)
                tree[str(node)][4] = True
        else:
            _ = stack.pop()
            alreadyStored = True
                
    return preOrderList

def postOrderTraversal(tree):
    postOrderList, stack = [], [0]
    
    # Traverse all nodes in tree
    while len(stack) != 0:
        # Peek the top of the stack
        node = stack[-1]
        
        # See the left and right childen and if they were visited
        leftChild, leftChildVisited = tree[str(node)][1], tree[str(node)][2]
        rightChild, rightChildVisited = tree[str(node)][3], tree[str(node)][4]
        
        # If the left child is valid and it hasn't been visited,
        # then add it to the top of the stack and visit it
        if (leftChild != -1) and (leftChildVisited == False):
            stack.append(leftChild)
            tree[str(node)][2] = True
        # Otherwise, if the right child is valid and it hasn't been visited,
        # then add that to the top of the stack
        elif (rightChild != -1) and (rightChildVisited == False):
            stack.append(rightChild)
            tree[str(node)][4] = True
        else:
            postOrderList.append(tree[str(stack.pop())][0])

    return postOrderList


### START OF PROGRAM ###
n = int(input())
tree = {}

# Record vertexs and add additional fields (LeftChildVisited, RightChildVisited)
for i in range(n):
    tree[str(i)] = [int(x) for x in input().split()]
    tree[str(i)].append(False)                                            # LeftChildVisited
    tree[str(i)][2], tree[str(i)][3] = tree[str(i)][3], tree[str(i)][2]
    tree[str(i)].append(False)                                            # RightChildVisited

print(*inOrderTraversal(copy.deepcopy(tree)))
print(*preOrderTraversal(copy.deepcopy(tree)))
print(*postOrderTraversal(copy.deepcopy(tree)))
