# Uses python3
import numpy as np

# s = number of segments; p = number of points to check
[s,p] = [int(x) for x in input().split()]

# Record the segments
segs = np.zeros((s,2),dtype=int)
[lowerBound, upperBound] = [int(x) for x in input().split()]
segs[0][0], segs[0][1] = lowerBound, upperBound
if s > 1:
    for i in range(s-1):
        segs[i+1][0],segs[i+1][1] = [int(x) for x in input().split()]
        if segs[i+1][0] < lowerBound:
            lowerBound = segs[i+1][0]
        if segs[i+1][1] > upperBound:
            upperBound = segs[i+1][1]

# Create and store amount of segment overlaps in new count matrix
count = np.zeros(abs(upperBound - lowerBound + 1),dtype=int)
for i in range(s):
    count[(segs[i][0]-lowerBound):(segs[i][1]-lowerBound+1)] += 1

# Check lottery holders and see if they won
ticketNums = [int(x) for x in input().split()]
winnings = np.zeros((p),dtype=int)
for i in range(p):
    if ticketNums[i] > upperBound or ticketNums[i] < lowerBound:
        winnings[i] = 0
    else:
        winnings[i] = count[ticketNums[i] - lowerBound]

for x in winnings:
    print(x, end = " ")
