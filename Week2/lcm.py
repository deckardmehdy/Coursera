# Uses python3

def lcm(a,b):
    lcm = a
    while (lcm % b) != 0:
        lcm += a
    return lcm

nums = [int(x) for x in input().split()]
print(lcm(nums[0], nums[1]))
