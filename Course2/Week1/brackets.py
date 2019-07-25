# Runs using Python 3
class Stack:
    class Node:
        def __init__(self,data,index):
            self.data = data
            self.next = None
            self.index = index

    def __init__(self):
        self.top = None

    def push(self,data,index):
        newNode = self.Node(data,index)
        # If the stack isn't empty:
        if self.top != None:
            newNode.next = self.top
        self.top = newNode

    def pop(self):
        # If the stack is empty:
        if self.top == None:
            return "Error!"
        else:
            item = self.top.data
            self.top = self.top.next
            return item

    def isEmpty(self):
        return (self.top == None)

def checkBrackets(S):
    # Create a new stack:
    myStack = Stack()
    n = len(S)

    # Loop through and find matching brackets:
    for i in range(n):
        # Opening brackets:
        if (S[i] == "(") or (S[i] == "{") or (S[i] == "["):
            myStack.push(S[i],(i+1))
        # Closing brackets:
        elif S[i] == ")":
            item = myStack.pop()
            if (item != "(") or (item == "Error!"):
                return (i+1)
        elif S[i] == "}":
            item = myStack.pop()
            if (item != "{") or (item == "Error!"):
                return (i+1)
        elif S[i] == "]":
            item = myStack.pop()
            if (item != "[") or (item == "Error!"):
                return (i+1)

    # After looping through, check if there are any remaining brackets left to match:
    if myStack.isEmpty() == False:
        # If there are any left, go to the bottom of the stack and
        # find the first unmatched opening bracket and return that:
        while myStack.top.next != None:
            _ = myStack.pop()
        return myStack.top.index

    # If there are no remaining ones, return success
    return("Success")


### START OF PROGRAM ###
S = str(input())
print(checkBrackets(S))
