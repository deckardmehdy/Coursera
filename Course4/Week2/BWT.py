# Runs using Python 3

def BWT(text):
    M = [text]
    T = len(text)
    
    # Go through and store all cyclic rotations of text
    for i in range(1,T):
        cycRot = text[i:T] + text[0:i]
        M.append(cycRot)

    # Sort the cyclic rotations
    M.sort()

    # Return the BWT
    lastCol = ""
    for i in range(T):
        lastCol += M[i][T-1]
    return lastCol

################################
####### START OF PROGRAM #######
################################
text = str(input())
print(BWT(text))
