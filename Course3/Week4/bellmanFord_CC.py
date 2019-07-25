# Runs using Python 3
import heapq, copy, numpy

### CONNECTED COMPONENTS METHODS ###

def edgeVisited(vertex,neighbor,dict):
    return dict[str(vertex) + "-" + str(neighbor)]

def visitEdge(vertex,neighbor,dict):
    dict[str(vertex) + "-" + str(neighbor)] = True
    return dict

def connectedComps(dict,n):
    # Do a depth first search of all of the vertices in the graph, starting with the last vertex
    # Store the connected components in individual lists
    dict["VTV"] = [False] * n
    dict["Explored"] = [False] * n
    connectedComps = []
    for i in range(n):
        if dict["VTV"][i] == False:
            # Create a new stack with a vertex that hasn't been visited
            # and a new connected component
            stack, connectedComp = [i+1], []
            dict["VTV"][i] = True
            while len(stack) > 0:
                # Peek at the top of the stack
                vertex = stack[-1]
                
                # Scan the adjacency list from the last adjacent vertex to the first and see
                # how many valid neighbors it has
                numOfNeighbors, validNeighborExists = len(dict[str(vertex)]), False
                while numOfNeighbors > 0:
                    neighbor = dict[str(vertex)][numOfNeighbors-1][0]
                    
                    # If the neighbor hasn't been visited, see if it creates a cycle.
                    # If it doesn't, then explore it; otherwise, ignore.
                    if (edgeVisited(vertex,neighbor,dict) == False) and (dict["Explored"][neighbor-1] == False):
                        dict = visitEdge(vertex,neighbor,dict)
                        if neighbor not in stack:
                            stack.append(neighbor)
                            validNeighborExists = True
                            numOfNeighbors = 0              # break out of the loop
                        # Take it out of the Vertex to Visit (VTV) list
                        # If it hasn't been visited yet
                        if dict["VTV"][neighbor-1] == False:
                            dict["VTV"][neighbor-1] = True
                    # If it has been visited, then decrement the numOfNeighbors
                    else:
                        numOfNeighbors -= 1
            
                # If a valid neighbor wasn't found, then pop the top of the stack
                # and put it in the list
                if validNeighborExists == False:
                    vertexToRemove = stack.pop()
                    if dict["Explored"][vertexToRemove-1] == False:
                        dict["Explored"][vertexToRemove-1] = True
                        connectedComp.append(vertexToRemove)

            # After going through the whole stack, reverse it
            # and add it to the connected components list
            connectedComp.reverse()
            connectedComps.append(connectedComp)

    # At the end, return the correct topology ordering
    return connectedComps

### CURRENCY CHECK METHODS ###

def checkCycles(prev,connectedComp,lastRelaxed):
    #visited = createVisited(connectedComp)
    visited = {}
    for i in range(len(connectedComp)+1):
        if lastRelaxed != None:
            if visited.get(str(lastRelaxed),False) == False:
                visited[str(lastRelaxed)] = True
                lastRelaxed = prev[lastRelaxed-1]
            else:
                return True
        else:
            return False
    return False

def createHeap(connectedComp):
    heap = []
    for i in range(len(connectedComp)):
        heap.append([16777215,connectedComp[i]])
    return heap
"""
def createVisited(connectedComp):
    visited = {}
    for i in range(len(connectedComp)):
        visited[str(connectedComp[i])] = False
    return visited

def resetVisited(visited,numsUsed):
    #print("Before: " + str(visited))
    #print("Nums used: " + str(numsUsed))
    while len(numsUsed) > 0:
        visited[numsUsed.pop()-1] = False
    #print("After: " + str(visited))
    return visited
"""
def currencyAnoms(dict,n,connectedComps):
    # Create an array which stores distances and previous nodes
    dist = [16777215] * n             # 16777215 = undiscovered
    prev = [None] * n
    lastRelaxed = None
    #visited = [False] * n
    
    # Explore each connected component (greater than size 1) and see if any
    # negative cycles exist within any of them
    for CC in range(len(connectedComps)):
        lastRelaxed = None
        #print("Connected component #" + str(CC) + " : " + str(connectedComps[CC]))
        # Repeat cycle V-1 times for all vertexs in the connected component:
        for j in range(len(connectedComps[CC])):
            #print("Distances before iteration " + str(j+1) + " :" + str(dist))
            changes = 0
            #numsUsed,numsUsedDict = [],{}
            visited = {}
            # Create a new heap (list) and visited flags (dict)
            heap = createHeap(connectedComps[CC])
            #visited = createVisited(connectedComps[CC])
            #visited = numpy.zeros((n),dtype=int) # Restart it
            #visited = (visited == False)
                
            # Make the first node's distance zero
            # and push it to the top of the queue
            firstNode = connectedComps[CC][j]
            dist[firstNode-1] = 0
            heapq.heappush(heap,[0,firstNode])

            # Explore all nodes in connected component
            while len(heap) > 0:
                #print(heap)
                # Pop the top of the heap and explore
                # if it hasn't been visited already:
                [_,vertex] = heapq.heappop(heap)
                if visited.get(str(vertex),False) == False:
                    #numsUsed.append(vertex)
                    visited[str(vertex)] = True
                    numOfEdges = len(dict[str(vertex)])
                    # Loop through all of the edges
                    # and relax any if possible:
                    for i in range(numOfEdges):
                        neighbor = dict[str(vertex)][i][0]
                        edgeWeight = dict[str(vertex)][i][1]
                        # If the edge can be relax, update the
                        # distance val and push onto the heap:
                        if dist[neighbor-1] > (dist[vertex-1] + edgeWeight):
                            #print("Edge between " + str(vertex) + " and " + str(neighbor) + " being relaxed. " + str(dist[neighbor-1]) + " > (" + str(dist[vertex-1]) + " + " + str(edgeWeight) + ")")
                            dist[neighbor-1] = dist[vertex-1] + edgeWeight
                            prev[neighbor-1] = vertex
                            changes += 1
                            if visited.get(str(neighbor),False) == False:
                                heapq.heappush(heap,[dist[neighbor-1],neighbor])
                            lastRelaxed = neighbor

            # If no changes were made, then break from the loop
            if changes == 0:
                j = len(connectedComps[CC])
    
        if checkCycles(prev,connectedComps[CC],lastRelaxed) == True:
            return 1

    # If all of the connected components have been searched
    # and no neg cycles were found, return 0
    return 0

################################
####### START OF PROGRAM #######
################################
[n,m] = [int(x) for x in input().split()]

# Initialize a dictionary with n vertices
dict = {}
for i in range(1,(n+1)):
    dict[str(i)] = []

# Store edges and their weights:
for i in range(m):
    # u = starting vertex; v = ending vertex; e = edge weight
    [u,v,e] = [int(x) for x in input().split()]
    
    # Store the edge in the adjacency list
    dict[str(u)].append([v,e])

    # Store a visited variable for the edge
    # Storage format: dict["u-v"]
    dict[str(u) + "-" + str(v)] = False

# Compute the connected components in the dict
CCs = connectedComps(copy.deepcopy(dict),n)

# See if there are any anomolies in the currency exchange
# 0 = none found; 1 = found
print(currencyAnoms(dict,n,CCs))
