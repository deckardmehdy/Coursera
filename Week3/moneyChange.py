# Uses python3

def calc_coins(money):
    numOfCoins = 0
    while money > 0:
        if money >= 10:
            numOfCoins = numOfCoins + money//10
            money = money % 10
        elif money < 10 and money >= 5:
            numOfCoins = numOfCoins + money//5
            money = money % 5
        elif money < 5:
            numOfCoins = numOfCoins + money//1
            money = 0
    return numOfCoins

money = int(input())
print(calc_coins(money))
