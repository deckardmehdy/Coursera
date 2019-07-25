# python3
import numpy as np

def digitsAndOps(s):
    n = len(s)
    digits,operands = [],[]
    for i in range(n):
        if (i % 2) == 0:        # even = digit
            digits.append(int(s[i]))
        else:                   # odd = operand
            operands.append(str(s[i]))
    return [digits,operands]

def expression(num1,operand,num2):
    if operand == "+":          # add
        return (num1 + num2)
    elif operand == "*":        # multiply
        return (num1 * num2)
    else:                       # subtract
        return (num1 - num2)

def minAndMax(i,j,M,m,operands):
    minNum =  100000
    maxNum = -100000
    for k in range(i,j):
        #print("k = " + str(k))
        a = expression(M[i,k],operands[k],M[(k+1),j])
        #print("a = " + str(M[i,k]) + str(operands[k]) + str(M[(k+1),j]))
        b = expression(M[i,k],operands[k],m[(k+1),j])
        #print("b = " + str(M[i,k]) + str(operands[k]) + str(m[(k+1),j]))
        c = expression(m[i,k],operands[k],M[(k+1),j])
        #print("c = " + str(m[i,k]) + str(operands[k]) + str(M[(k+1),j]))
        d = expression(m[i,k],operands[k],m[(k+1),j])
        #print("d = " + str(m[i,k]) + str(operands[k]) + str(m[(k+1),j]))
        minNum = min(minNum,a,b,c,d)
        maxNum = max(maxNum,a,b,c,d)
    return [minNum,maxNum]

def parentheses(digits,operands):
    n = len(digits)
    M = np.zeros((n,n),dtype=int)
    m = np.zeros((n,n),dtype=int)

    # Initialize min and max matrices
    for i in range(n):
        m[i,i] = digits[i]
        M[i,i] = digits[i]

    # Loop through
    for s in range(1,n):
        for i in range(n-s):
            j = i + s
            #print("i = " + str(i) + "; j = " + str(j))
            [minNum,maxNum] = minAndMax(i,j,M,m,operands)
            m[i,j],M[i,j] = minNum,maxNum
    return M[0,(n-1)]

### START OF PROGRAM ###
s = str(input())
[digits,operands] = digitsAndOps(s)
if len(s) == 3:
    print(expression(digits[0],operands[0],digits[1]))
else:
    print(parentheses(digits,operands))
