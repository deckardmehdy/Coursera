# Uses python3

def calc_last_fib_digit(n):
    a,b,c,count = 0, 1, 1, 2
    while count < n:
        a = b
        b = c
        c = (b + a) % 10
        count += 1
    return c

n = int(input())
if n > 1:
    print(calc_last_fib_digit(n))
else:
    print(n)
