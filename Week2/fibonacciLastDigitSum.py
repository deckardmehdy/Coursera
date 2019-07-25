# Uses python3

def calc_last_fib_digit_sum(n):
    a,b,c,count = 0, 1, 2, 2
    while count < n:
        a = b
        b = c
        c = (b + a + 1) % 10
        count += 1
    return c

n = int(input())
if n > 2:
    print(calc_last_fib_digit_sum(n))
else:
    print(n)
