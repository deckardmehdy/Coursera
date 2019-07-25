# Uses python3

def calc_fib(n):
    global memo
    c = memo[n]
    if n > 1 and c == 0:
        c = calc_fib(n-1) + calc_fib(n-2)
        memo[n] = c
    return c

n = int(input())
memo = [0] * (n+1)
if n > 0:
    memo[1] = 1
    print(calc_fib(n))
else:
    print(0)
