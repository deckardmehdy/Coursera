# python3

def max_pairwise_product(numbers,n):
    biggestNum = 0;
    secondBiggestNum = 0;
    
    for x in range(n):
        if numbers[x] >= biggestNum:
            secondBiggestNum = biggestNum
            biggestNum = numbers[x]
        elif numbers[x] >= secondBiggestNum:
            secondBiggestNum = numbers[x]
3
    return (biggestNum * secondBiggestNum)

if __name__ == '__main__':
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(numbers,n))
