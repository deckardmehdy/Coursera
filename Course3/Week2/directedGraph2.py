# Runs using Python 3

def edgeVisited(vertex,neighbor,dict):
    return dict[str(vertex) + "-" + str(neighbor)]

def visitEdge(vertex,neighbor,dict):
    dict[str(vertex) + "-" + str(neighbor)] = True
    return dict

def computeTopology(dict,n,verticesToVisit):
    # Do a depth first search of all of the vertices
    # in the graph, starting with the last vertex
    topOrder = [0] * n
    j = n - 1
    for i in range(n):
        if dict["VTV"][i] == False:
            # Create a new stack with a vertex that hasn't been visited
            stack = [i+1]
            dict["VTV"][i] = True
            while len(stack) > 0:
                # Peek at the top of the stack
                vertex = stack[-1]

                # Scan the adjacency list from the last adjacent vertex to
                # the first and see how many valid neighbors it has
                numOfNeighbors, validNeighborExists = len(dict[str(vertex)]), False
                while numOfNeighbors > 0:
                    neighbor = dict[str(vertex)][numOfNeighbors-1]
                    
                    # If the neighbor hasn't been visited, see if it creates a cycle.
                    # If it doesn't, then explore it; otherwise, ignore.
                    if (edgeVisited(vertex,neighbor,dict) == False) and (dict["o" + str(neighbor)] == False):
                        dict = visitEdge(vertex,neighbor,dict)
                        if neighbor not in stack:
                            stack.append(neighbor)
                            validNeighborExists = True
                            numOfNeighbors = 0              # break out of the loop
                        # Take it out of the Vertex to Visit list
                        if dict["VTV"][neighbor-1] == False:
                            dict["VTV"][neighbor-1] = True
                    # If it has been visited, then decrement the numOfNeighbors
                    else:
                        numOfNeighbors -= 1

                # If a valid neighbor wasn't found, then pop the top of the stack
                # and put it in the list
                if validNeighborExists == False:
                    vertexToRemove = stack.pop()
                    if dict["o" + str(vertexToRemove)] == False:
                        dict["o" + str(vertexToRemove)] = True
                        topOrder[j] = vertexToRemove
                        j -= 1

    # At the end, return the correct topology ordering
    return topOrder

### START OF PROGRAM ###
[n,m] = [int(x) for x in input().split()]

# Initialize a dictionary with n vertices
dict, verticesToVisit = {}, []
dict["VTV"] = [False] * n       # vertexs to visit
for i in range(1,(n+1)):
    dict[str(i)] = []
    dict["o" + str(i)] = False
    verticesToVisit.append(i)

# Store edges and their visited variables
for i in range(m):
    [u,v] = [int(x) for x in input().split()]
    
    # Store the edge in the adjacency lists
    dict[str(u)].append(v)

    # Store a visited variable for the edge
    # Storage format: dict["u-v"]
    dict[str(u) + "-" + str(v)] = False

print(*computeTopology(dict,n,verticesToVisit))
