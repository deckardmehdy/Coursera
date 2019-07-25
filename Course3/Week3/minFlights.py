# Runs using Python 3
import queue

def minNumOfFlights(dict,n,u,v):
    myQueue = queue.Queue()
    distance = [-1] * n             # -1 = undiscovered
    distance[u-1] = 0               # Start
    myQueue.put(u)

    while myQueue.empty() == False:
        vertex = myQueue.get()
        numOfNeighbors = len(dict[str(vertex)])
        for i in range(numOfNeighbors):
            neighbor = dict[str(vertex)][i]
            # If the neighbor hasn't been discovered yet:
            if distance[neighbor-1] == -1:
                myQueue.put(neighbor)
                distance[neighbor-1] = distance[vertex-1] + 1

    return distance[v-1]

### START OF PROGRAM ###
[n,m] = [int(x) for x in input().split()]

# Initialize a dictionary with n vertices
dict = {}
for i in range(1,(n+1)):
    dict[str(i)] = []

# Store edges and their visited variables
for i in range(m):
    [u,v] = [int(x) for x in input().split()]
    
    # Store the edges in the adjacency lists
    dict[str(u)].append(v)
    dict[str(v)].append(u)

# Aquire vertices u and v to find
[u,v] = [int(x) for x in input().split()]

# Print the minimum num of flights
# -1 = not found
print(minNumOfFlights(dict,n,u,v))
