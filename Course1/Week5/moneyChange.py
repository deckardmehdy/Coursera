# Uses python3
import numpy as np

def get_change(money):
    minNumOfCoins = np.zeros((money+1),dtype=int) + money
    minNumOfCoins[0] = 0
    coins = [1,3,4]
    for m in range(1,(money+1)):
        for i in range(3):
            if m >= coins[i]:
                numOfCoins = minNumOfCoins[m-coins[i]] + 1
                if numOfCoins < minNumOfCoins[m]:
                    minNumOfCoins[m] = numOfCoins
    return minNumOfCoins[money]

# Start of function
money = int(input())
print(get_change(money))
