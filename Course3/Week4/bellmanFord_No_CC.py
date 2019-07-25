# Runs using Python 3
import heapq, numpy
"""
def makeSet(n):
    numpy.linspace(())

def currencyAnoms(dict,n):
            [_,vertex] = heapq.heappop(heap)
                        if visited.get(str(neighbor),False) == False:
                            heapq.heappush(heap,[dist[neighbor-1],neighbor])

"""
################################
####### START OF PROGRAM #######
################################
n = int(input())

# Record X and Y coordinates for n points
x = [] * n
y = [] * n
for i in range(n):
    [xi, yi] = [float(x) for x in input().split()]
    x[i], y[i] = xi, yi

print(x)
#[parent, rank] = makeSet(n)
