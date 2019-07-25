# Runs using Python 3
import queue

def minNumOfFlights(dict,n):
    myQueue = queue.Queue()
    distance = [-1] * n             # -1 = undiscovered

    # Loop through all vertices iterativly
    for i in range(n):
        # Only visit the vertex if it hasn't been discovered
        if distance[i] == -1:
            distance[i] = 0
            myQueue.put(i+1)
            while myQueue.empty() == False:
                vertex = myQueue.get()
                numOfNeighbors = len(dict[str(vertex)])
                for j in range(numOfNeighbors):
                    neighbor = dict[str(vertex)][j]
                    
                    # If the neighbor hasn't been discovered yet,
                    # Put it in the queue, and change its distance
                    if distance[neighbor-1] == -1:
                        myQueue.put(neighbor)
                        distance[neighbor-1] = distance[vertex-1] + 1
                    # If the neighbor has been discovered,
                    # Check that the color is correct
                    else:
                        if (distance[neighbor-1] % 2) == (distance[vertex-1] % 2):
                            return 0

    return 1

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


# Print the minimum num of flights
# -1 = not found
print(minNumOfFlights(dict,n))
