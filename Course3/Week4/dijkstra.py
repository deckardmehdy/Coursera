# Runs using Python 3
import heapq

def minFlightCost(dict,n,u,v,heap):
    # Create an array which stores distances,
    # previous nodes, and visited flags
    dist = [16777215] * n                       # 16777215 = undiscovered
    visited  = [False] * n
    #prev = [None] * n
    
    # Make the starting node's distance zero
    # and push it to the top of the queue
    dist[u-1] = 0
    heapq.heappush(heap,[0,u])

    while len(heap) > 0:
        # Pop the top of the heap and explore
        # if it hasn't been visited already:
        [distance,vertex] = heapq.heappop(heap)
        if visited[vertex-1] == False:
            visited[vertex-1] = True
            numOfEdges = len(dict[str(vertex)])
            # Loop through all of the edges
            # and relax any if possible:
            for i in range(numOfEdges):
                neighbor = dict[str(vertex)][i][0]
                edgeWeight = dict[str(vertex)][i][1]
                # If the edge can be relax, update the
                # distance val and push onto the heap:
                if dist[neighbor-1] > (dist[vertex-1] + edgeWeight):
                    dist[neighbor-1] = dist[vertex-1] + edgeWeight
                    #prev[neighbor-1] = u
                    heapq.heappush(heap,[dist[neighbor-1],neighbor])

    return dist[v-1]

### START OF PROGRAM ###
[n,m] = [int(x) for x in input().split()]

# Initialize a dictionary and heap with n vertices
dict, heap = {}, []
for i in range(1,(n+1)):
    dict[str(i)] = []
    heapq.heappush(heap,[16777215,i])

# Store edges and their weights:
for i in range(m):
    # u = starting vertex; v = ending vertex; e = edge weight
    [u,v,e] = [int(x) for x in input().split()]
    
    # Store the edge in the adjacency list
    dict[str(u)].append([v,e])

# Vertices to find: u and v
[u,v] = [int(x) for x in input().split()]

# Print the minimum cost of flights
# -1 = not found
c = minFlightCost(dict,n,u,v,heap)
if c == 16777215:
    print(-1)
else:
    print(c)
