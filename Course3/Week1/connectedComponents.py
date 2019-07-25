# Runs using Python 3

def edgeVisited(vertex,neighbor,dict):
    if vertex < neighbor:
        return dict[str(vertex) + "-" + str(neighbor)]
    else:
        return dict[str(neighbor) + "-" + str(vertex)]

def visitEdge(vertex,neighbor,dict):
    if vertex < neighbor:
        dict[str(vertex) + "-" + str(neighbor)] = True
    else:
        dict[str(neighbor) + "-" + str(vertex)] = True
    return dict

def connectedComps(dict,n,verticesToVisit):
    # Do a depth first search of all of the vertices
    # in the graph, starting with the last vertex
    numOfComps = 0
    while len(verticesToVisit) > 0:
        # Create a new stack with a vertex that hasn't been visited
        # and increment the number of components found
        stack = [verticesToVisit.pop()]
        numOfComps += 1
        while len(stack) > 0:
            # Peek at the top of the stack
            vertex = stack[-1]

            # Scan the adjacency list from the last adjacent vertex to
            # the first and see how many valid neighbors it has
            numOfNeighbors, validNeighborExists = len(dict[str(vertex)]), False
            while numOfNeighbors > 0:
                neighbor = dict[str(vertex)][numOfNeighbors-1]
                
                # If the neighbor hasn't been visited, then visit the edge and put
                # the new vertex on top of the stack. Remove it from the list of
                # vertices left to visit, too.
                if edgeVisited(vertex,neighbor,dict) == False:
                    dict = visitEdge(vertex,neighbor,dict)
                    stack.append(neighbor)
                    validNeighborExists = True
                    if neighbor in verticesToVisit:
                        verticesToVisit.remove(neighbor)
                    numOfNeighbors = 0      # break out of the loop
                # If it has been visited, then decrement the numOfNeighbors
                else:
                    numOfNeighbors -= 1

            # If a valid neighbor wasn't found, then pop the top of the stack
            if validNeighborExists == False:
                _ = stack.pop()

    # After finishing, return the num of components found
    return numOfComps

### START OF PROGRAM ###
[n,m] = [int(x) for x in input().split()]

# Initialize a dictionary with n vertices
dict, verticesToVisit = {}, []
for i in range(1,(n+1)):
    dict[str(i)] = []
    verticesToVisit.append(i)

# Store edges and their visited variables
for i in range(m):
    [num1,num2] = [int(x) for x in input().split()]
    
    # Store them in the adjacency lists
    dict[str(num1)].append(num2)
    dict[str(num2)].append(num1)

    # Store one visited variable for the edge
    # Storage format: dict["smallNum-bigNum"]
    if num1 < num2:
        dict[str(num1) + "-" + str(num2)] = False
    else:
        dict[str(num2) + "-" + str(num1)] = False

print(connectedComps(dict,n,verticesToVisit))
