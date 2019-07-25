# Uses python3

def gcd(a,b):
    if b != 0:
        return gcd(b,(a % b))
    else:
        return a

nums = [int(x) for x in input().split()]
print(gcd(nums[0], nums[1]))
