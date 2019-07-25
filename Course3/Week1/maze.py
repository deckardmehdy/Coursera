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

def doesPathExist(u,v,dict):
    # Do a depth first search of all of the vertices
    # in the graph, starting with vertex U
    stack = [u]
    while len(stack) > 0:
        # Peek at the top of the stack
        vertex = stack[-1]

        # Scan the adjacency list from the last adjacent vertex to
        # the first and see how many valid neighbors it has
        numOfNeighbors, validNeighborExists = len(dict[str(vertex)]), False
        while numOfNeighbors > 0:
            neighbor = dict[str(vertex)][numOfNeighbors-1]
            
            # If the neighbor hasn't been visited, then see if it equals the
            # vertex we are looking for. If not, then visit the edge and put
            # the new vertex on top of the stack.
            if edgeVisited(vertex,neighbor,dict) == False:
                if neighbor == v:
                    return 1
                else:
                    dict = visitEdge(vertex,neighbor,dict)
                    stack.append(neighbor)
                    validNeighborExists = True
                    numOfNeighbors = 0      # break out of the loop
            # If it has been visited, then decrement the numOfNeighbors
            else:
                numOfNeighbors -= 1

        # If a valid neighbor wasn't found, then pop the top of the stack
        if validNeighborExists == False:
            _ = stack.pop()

    # If no path was found, return 0
    return 0

### START OF PROGRAM ###
[n,m] = [int(x) for x in input().split()]

# Initialize a dictionary with n vertices
dict = {}
for i in range(1,(n+1)):
    dict[str(i)] = []

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

[u,v] = [int(x) for x in input().split()]
print(doesPathExist(u,v,dict))
