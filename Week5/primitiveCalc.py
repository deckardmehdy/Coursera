# Uses python3
import numpy as np

def get_sequence(nums,n):
    minOperations = nums[0][n]
    sequence = np.zeros((minOperations+1),dtype=int)
    sequence[minOperations],sequence[0] = n,1
    pointer,seqPointer = n,(minOperations-1)
    minOperations = seqPointer
    while minOperations > 0:
        pointer = nums[1][pointer]
        sequence[seqPointer] = pointer
        minOperations -= 1
        seqPointer -= 1
    return sequence

def calc_operations(n):
    nums = np.zeros((2,(n+1)),dtype=int) + n
    nums[0][0],nums[0][1],nums[1][0],nums[1][1] = 0,0,0,0
    for currentNum in range(2,(n+1)):
        for operation in range(1,4):
            # Operation 1: addtion of 1
            if operation == 1:
                minOperations = nums[0][currentNum-1] + 1
                if minOperations < nums[0][currentNum]:
                    nums[0][currentNum] = minOperations
                    nums[1][currentNum] = currentNum - 1
            # Operation 2: multiplying by 2
            elif operation == 2 and ((currentNum % 2) == 0):
                minOperations = nums[0][int(currentNum/2)] + 1
                if minOperations < nums[0][currentNum]:
                    nums[0][currentNum] = minOperations
                    nums[1][currentNum] = currentNum / 2
            # Operation 3: multiplying by 3
            elif operation == 3 and ((currentNum % 3) == 0):
                minOperations = nums[0][int(currentNum/3)] + 1
                if minOperations < nums[0][currentNum]:
                    nums[0][currentNum] = minOperations
                    nums[1][currentNum] = currentNum / 3
    sequence = get_sequence(nums,n)
    return([nums[0][n],sequence])
    # call method that goes through the nums array and returns an array of values to be printed
    # insert return statement

### START OF FILE: ###
# Get integer
n = int(input())

# Get min number of operations and print the sequence of
if n == 1:
    print(0)
    print(1)
else:
    minOperations,sequence = calc_operations(n)
    print(minOperations)
    for num in sequence:
        print(num, end = " ")
    print("")
