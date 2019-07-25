# Uses python3

def fib_partial_sum(start,end):
    if start > 2:
        lastDigStart = calc_last_fib_digit_sum(start-1)
    else:
        lastDigStart = start

    if end > 2:
        lastDigEnd = calc_last_fib_digit_sum(end)
    else:
        lastDigEnd = end

    newDigit = (lastDigEnd - lastDigStart) % 10

    if newDigit >= 0:
        return newDigit
    else:
        return (10+newDigit)


def calc_last_fib_digit_sum(n):
    a,b,c,count = 0, 1, 2, 2
    while count < n:
        a = b
        b = c
        c = (b + a + 1) % 10
        count += 1
    return c

def calc_last_fib_digit(n):
    a,b,c,count = 0, 1, 1, 2
    while count < n:
        a = b
        b = c
        c = (b + a) % 10
        count += 1
    return c

n = [int(x) for x in input().split()]
if (n[1] - n[0]) != 0:
    print(fib_partial_sum(n[0],n[1]))
else:
    if n[0] > 2:
        print(calc_last_fib_digit(n[0]))
    else:
        print(n[0])
