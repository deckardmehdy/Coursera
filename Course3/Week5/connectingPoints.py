# Runs using Python 3
import heapq, math
import numpy as np

def makeSet(n):
    parent = np.linspace(0,(n-1),n,dtype=int)
    rank = [0] * n
    return [parent,rank]

def find(i,parent):
    if i != parent[i]:
        [parent[i],parent] = find(parent[i],parent)
    return [parent[i],parent]

def union(i,j,parent,rank):
    [i,parent] = find(i,parent)
    [j,parent] = find(j,parent)
    if i == j:
        return [parent,rank]
    if rank[i] > rank[j]:
        parent[j] = i
    else:
        parent[i] = j
        if rank[i] == rank[j]:
            rank[j] += 1
    return [parent,rank]

def makeEdges(x,y,n):
    heap = []
    for i in range(n-1):
        for j in range((i+1),n):
            dist = math.hypot((x[j]-x[i]),(y[j]-y[i]))
            heapq.heappush(heap,[dist,i,j])
    return heap

def findMST(x,y,n):
    # Make a set given the number of coordinates
    [parent,rank] = makeSet(n)
    #print(parent)
    
    # Create a variable to store the total distance of the MST
    totalDist = 0

    # Calculate all of the edges and store them in a min-heap
    heap = makeEdges(x,y,n)

    # Go through all possible edges, in order of decreasing value
    # Add them to the MST if they don't form a cycle
    while len(heap) > 0:
        [dist,i,j] = heapq.heappop(heap)
        [parentI,parent] = find(i,parent)
        [parentJ,parent] = find(j,parent)
        #print("Parent of " + str(i) + " is " + str(parentI) + " and parent of " + str(j) + " is " + str(parentJ) + ".")
        if parentI != parentJ:
            #print("Creating a union between " + str(i) + " and " + str(j) + ".")
            totalDist += dist
            #print("Total distance is now " + str(totalDist))
            [parent,rank] = union(i,j,parent,rank)
            #print("New parent list is " + str(parent) + ". New rank list is " + str(rank))

    return totalDist

################################
####### START OF PROGRAM #######
################################
n = int(input())

# Record X and Y coordinates for n points
x = [0] * n
y = [0] * n
for i in range(n):
    [x[i], y[i]] = [float(int(z)) for z in input().split()]

print("%.7f" % findMST(x,y,n))
