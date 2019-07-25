# Uses python3
# import numpy as np

def calc_num_of_stops(tankMileage,numOfStations,stationLocs):
    numOfRefills, currentRefill = 0, 0
    while currentRefill < numOfStations:
        lastRefill = currentRefill
        while currentRefill < numOfStations and stationLocs[currentRefill + 1] - stationLocs[lastRefill] <= tankMileage:
            currentRefill = currentRefill + 1
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= numOfStations:
            numOfRefills = numOfRefills + 1
    return numOfRefills


# Start of Function
milesToDest = int(input())
tankMileage = int(input())
numOfStations = int(input())
stationLocs = [int(x) for x in input().split()]
stationLocs.append(milesToDest)
stationLocs.append(tankMileage+1)
if milesToDest <= tankMileage:
    print(0)
else:
    print(calc_num_of_stops(tankMileage,numOfStations,stationLocs))
