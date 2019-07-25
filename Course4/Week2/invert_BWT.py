# Runs using Python 3

def createFO(count):
    letters, start = ["A","C","G","T"], 1
    firstOcc = {"A": 0, "C": 0, "G": 0, "T": 0}
    for i in range(4):
        if count[letters[i]] != 0:
            firstOcc[letters[i]] = start
            start += count[letters[i]]
    return firstOcc

def invert_BWT(lastCol):
    # Make a dict for storing position and count of letters
    count = {"A": 0, "C": 0, "G": 0, "T": 0}
    lastColOccs = []
    for i in range(len(lastCol)):
        if lastCol[i] != "$":
            lastColOccs.append(count[lastCol[i]])
            count[lastCol[i]] += 1
        else:
            lastColOccs.append(0)

    # Create dict of first occurances
    firstOcc = createFO(count)

    # Reconstruct string:
    string = "$"
    pointer = 0
    while len(string) < len(BWT):
        # Get the corresonding letter in last column
        letter = lastCol[pointer]
        occurance = lastColOccs[pointer]

        # Find the location of the letter in the first column
        pointer = firstOcc[letter] + occurance
        
        # Add the letter to the string
        string += letter

    string = string[::-1]
    return string


################################
####### START OF PROGRAM #######
################################
BWT = str(input())
print(invert_BWT(BWT))
