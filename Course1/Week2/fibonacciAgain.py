# Uses python3

def calc_period_length(modulus):
    a,b,c, length = 0, 1, 1, 2
    modB, modC = 1, 1
    global fibMods
    
    while ((modB != 0) or (modC != 1)):
        # Add new modulus to the end of the list
        fibMods.append(modC)
        length = length + 1
        
        # Calculate a new fib number
        a = b
        b = c
        c = b + a
        
        # Calculate the modulus of the new fib number
        modB = modC
        modC = c % modulus
    
    # Delete the last element of the list and decrement the length by 1
    del fibMods[-1]
    
    return (length - 1)

nums = [int(x) for x in input().split()]
fibMods = [0,1]

# nums[0] = integer n; nums[1] = modulus
length = calc_period_length(nums[1])

arrayElement = nums[0] % length
print(fibMods[arrayElement])
