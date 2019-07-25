# Uses python3
import random

def partition3(l, r):
    global A
    x = A[l]
    m1, m2 = l,l
    for i in range(l + 1, r + 1):
        a = A[i]
        if a < x:
            A.insert(m1,A.pop(i))
            m1 += 1
            m2 += 1
        elif a == x:
            m2 += 1
    return [m1, m2]

def randomized_quick_sort(l, r):
    global A
    if l >= r:
        return
    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]
    [m1, m2] = partition3(l, r)
    randomized_quick_sort(l, m1 - 1)
    randomized_quick_sort(m2 + 1, r)

n = int(input())
A = [int(x) for x in input().split()]
randomized_quick_sort(0, n - 1)
for a in A:
    print(a, end = " ")
print(" ")
