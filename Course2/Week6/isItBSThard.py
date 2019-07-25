# python3

def inOrderTraversal(tree):
    inOrderList, stack = [], [0]
    
    # Traverse all nodes in tree
    while len(stack) != 0:
        # Peek at the top of the stack
        node = stack[-1]
        nodeKey = tree[str(node)][0]
        
        # See the left and right childen and if they were visited
        leftChild, leftChildVisited = tree[str(node)][1], tree[str(node)][2]
        rightChild = tree[str(node)][3]

        # If the left child is valid and it hasn't been visited,
        # then add it to the top of the stack and visit it
        if (leftChild != -1) and (leftChildVisited == False):
            stack.append(leftChild)
            tree[str(node)][2] = True
            
            leftChildKey = tree[str(leftChild)][0]
            if leftChildKey >= nodeKey:
                return ["INCORRECT", inOrderList]
        # Otherwise, pop the current node
        else:
            inOrderList.append(tree[str(stack.pop())][0])
            # If it has a right child, then add that to the top of the stack
            if rightChild != -1:
                stack.append(rightChild)
                rightChildKey = tree[str(rightChild)][0]
                if nodeKey > rightChildKey:
                    return ["INCORRECT", inOrderList]

    return ["CORRECT", inOrderList]

def checkIfBST(inOrderList,n):
    for i in range(n-1):
        if inOrderList[i] > inOrderList[i+1]:
            return "INCORRECT"
    return "CORRECT"

### START OF PROGRAM ###
n = int(input())
if n == 0:
    print("CORRECT")
else:
    tree = {}
    
    # Record vertexs and add additional fields (LeftChildVisited, RightChildVisited)
    for i in range(n):
        tree[str(i)] = [int(x) for x in input().split()]
        tree[str(i)].append(False)                                            # LeftChildVisited
        tree[str(i)][2], tree[str(i)][3] = tree[str(i)][3], tree[str(i)][2]
        tree[str(i)].append(False)                                            # RightChildVisited

    [ans,inOrderList] = inOrderTraversal(tree)
    if ans == "CORRECT":
        print(checkIfBST(inOrderList,n))
    else:
        print(ans)
